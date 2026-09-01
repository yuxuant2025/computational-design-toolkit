import Rhino
import Rhino.Geometry as rg
import Rhino.Geometry.Intersect as ri
import scriptcontext as sc

# ── INPUTS ────────────────────────────────────────────────
# geo     — Surface / Brep / Mesh   (No type hint)
#           feed a Surface/Brep for SMOOTH curves (direct NURBS cut)
# spacing — float  Z pitch: top-to-top distance between steps.
# gap     — float  empty Z space between steps (step height = spacing-gap)
# depth   — float  horizontal tread depth (the RED dimension).
#                  leave at 0 to auto-default to spacing*2
# ─────────────────────────────────────────────────────────

slabs = []
log   = []

tol      = sc.doc.ModelAbsoluteTolerance
_spacing = float(spacing)
try:
    _depth = float(depth)
except (NameError, TypeError):
    _depth = 0.0
try:
    _gap = float(gap)
except (NameError, TypeError):
    _gap = 0.0

raw = geo.Value if hasattr(geo, "Value") else geo
log.append("input type: {}".format(type(raw).__name__))

# ── coerce to a Brep for smooth (mesh-free) intersection ──
if   isinstance(raw, rg.Brep):    brep = raw
elif isinstance(raw, rg.Surface): brep = raw.ToBrep()
else:                             brep = None        # Mesh input

# ── prepare a mesh only if we have no brep (or as fallback) ─
mesh = None
if isinstance(raw, rg.Mesh):
    mesh = rg.Mesh()
    mesh.Append(raw)
    mesh.Weld(0.1)

if brep is None and mesh is None:
    debug = "\n".join(log) + "\nFAIL: unsupported input"
else:
    bbox  = (brep or mesh).GetBoundingBox(True)
    diag  = bbox.Min.DistanceTo(bbox.Max)
    z_min = bbox.Min.Z
    z_max = bbox.Max.Z
    step   = max(_spacing, tol)
    slab_h = max(step - _gap, tol)
    _count = max(1, int((z_max - z_min) / step))

    if _depth <= 0:
        _depth = step * 2.0
    half  = _depth * 0.5
    style = rg.CurveOffsetCornerStyle.Sharp

    # ── decide intersection mode with a probe at mid-height ─
    mode = "mesh"
    if brep is not None:
        zt = (z_min + z_max) * 0.5
        pt = rg.Plane(rg.Point3d(0, 0, zt), rg.Vector3d.ZAxis)
        rc = ri.Intersection.BrepPlane(brep, pt, tol)
        if rc[0] and rc[1] and len(rc[1]) > 0:
            mode = "brep"            # smooth NURBS cut works

    # build a fine fallback mesh if brep cut failed
    if mode == "mesh" and mesh is None:
        mp = rg.MeshingParameters()
        mp.Tolerance         = diag * 0.0006
        mp.MaximumEdgeLength = diag * 0.008
        mp.JaggedSeams       = False
        mp.RefineGrid        = True
        mesh = rg.Mesh()
        for x in (rg.Mesh.CreateFromBrep(brep, mp) or []):
            mesh.Append(x)
        mesh.Weld(0.1)

    log.append("mode={}  Z {:.2f}-{:.2f}  spacing {:.3f}  gap {:.3f}  "
               "step_h {:.3f}  count {}  depth {:.3f}".format(
               mode, z_min, z_max, step, _gap, slab_h, _count, _depth))

    # ── get section curves at a plane (smooth if brep mode) ──
    def sections_at(plane):
        if mode == "brep":
            rc = ri.Intersection.BrepPlane(brep, plane, tol)
            if rc[0] and rc[1]:
                return list(rc[1])
            return []
        out = []
        pls = ri.Intersection.MeshPlane(mesh, plane)
        if pls:
            for pl in pls:
                if pl is not None and pl.Count >= 2:
                    c = pl.ToNurbsCurve()
                    if c:
                        out.append(c)
        return out

    # ── smooth ONLY faceted (degree-1) curves from a mesh ────
    def clean(crv):
        if crv.Degree > 1:
            return crv                       # already smooth NURBS
        length = crv.GetLength()
        n = max(min(int(length / max(step, tol)), 120), 8)
        rb = crv.Rebuild(n, 3, True)
        return rb if rb else crv

    def offset_side(crv, dist, plane):
        res = crv.Offset(plane, dist, tol, style)
        if not res:
            return None
        if len(res) == 1:
            return res[0]
        j = rg.Curve.JoinCurves(res, tol * 5)
        return j[0] if j else res[0]

    def tread_outline(crv, plane):
        crv = clean(crv)
        oc = offset_side(crv,  half, plane)
        ic = offset_side(crv, -half, plane)
        if oc is None or ic is None:
            return None
        if crv.IsClosed:
            return [oc, ic]
        ic_rev = ic.DuplicateCurve()
        ic_rev.Reverse()
        cap1 = rg.LineCurve(oc.PointAtEnd,     ic_rev.PointAtStart)
        cap2 = rg.LineCurve(ic_rev.PointAtEnd, oc.PointAtStart)
        loop = rg.Curve.JoinCurves([oc, cap1, ic_rev, cap2], tol * 5)
        if loop and loop[0].IsClosed:
            return [loop[0]]
        return None

    levels   = 0
    ok       = 0
    fat      = 0
    off_fail = 0

    for i in range(_count):
        z     = z_min + step * i + step * 0.5
        plane = rg.Plane(rg.Point3d(0, 0, z), rg.Vector3d.ZAxis)

        crvs = sections_at(plane)
        if not crvs:
            continue

        joined = rg.Curve.JoinCurves(crvs, step * 0.5) or crvs
        levels += 1

        for crv in joined:
            try:
                boundary = tread_outline(crv, plane)
            except:
                boundary = None
            if not boundary:
                off_fail += 1
                continue

            perimeter     = sum(c.GetLength() for c in boundary)
            expected_area = (perimeter / 2.0) * _depth

            planar = rg.Brep.CreatePlanarBreps(boundary, tol)
            if not planar:
                continue

            for pb in planar:
                if pb is None or not pb.IsValid:
                    continue
                ap = rg.AreaMassProperties.Compute(pb)
                if ap is None:
                    continue
                if ap.Area > expected_area * 2.5:
                    fat += 1
                    continue

                pb.Translate(rg.Vector3d(0, 0, -slab_h * 0.5))
                for face in pb.Faces:
                    s = rg.Brep.CreateFromOffsetFace(
                            face, slab_h, tol, False, True)
                    if s and s.IsValid:
                        slabs.append(s)
                        ok += 1
                        break

    log.append("levels={} slabs={} fat_rejected={} offset_fail={}".format(
        levels, ok, fat, off_fail))
    debug = "\n".join(log)