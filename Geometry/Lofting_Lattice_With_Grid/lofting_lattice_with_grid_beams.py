"""
Parametric Box with Grid Beams — GhPython Component
=====================================================
INPUTS:
  brep       : Brep  - Outer boundary (bounding box derived from it)
  loft       : Brep  - Closed lofted solid (grid trimmed at its surface)
  grid_space : float - Grid spacing in ft
  bw         : float - Beam cross-section width  (ft)
  bh         : float - Beam cross-section height (ft)

OUTPUTS:
  a : grid_lines — Trimmed grid lines (curves)
  b : beams      — Rectangular beam extrusions (Breps)
"""

import Rhino.Geometry as rg

tol = 0.001

# ================================================================
# GROUP 1 — DERIVE DIMENSIONS FROM BOUNDARY BREP
# ================================================================
bbox   = brep.GetBoundingBox(True)
min_pt = bbox.Min
max_pt = bbox.Max

L  = max_pt.X - min_pt.X
W  = max_pt.Y - min_pt.Y
H  = max_pt.Z - min_pt.Z
gs = grid_space
ox, oy, oz = min_pt.X, min_pt.Y, min_pt.Z


# ================================================================
# GROUP 3 — BUILD FULL GRID LINES
# ================================================================
def grid_vals(span, step):
    vals, v = [], 0.0
    while v <= span + 1e-6:
        vals.append(v)
        v += step
    return vals

xs = grid_vals(L, gs)
ys = grid_vals(W, gs)
zs = grid_vals(H, gs)

raw_lines = []
for yy in ys:
    for zz in zs:
        ln = rg.Line(rg.Point3d(ox,      oy + yy, oz + zz),
                     rg.Point3d(ox + L,  oy + yy, oz + zz))
        raw_lines.append(ln.ToNurbsCurve())
for xx in xs:
    for zz in zs:
        ln = rg.Line(rg.Point3d(ox + xx, oy,      oz + zz),
                     rg.Point3d(ox + xx, oy + W,  oz + zz))
        raw_lines.append(ln.ToNurbsCurve())
for xx in xs:
    for yy in ys:
        ln = rg.Line(rg.Point3d(ox + xx, oy + yy, oz),
                     rg.Point3d(ox + xx, oy + yy, oz + H))
        raw_lines.append(ln.ToNurbsCurve())

# ================================================================
# GROUP 4 — TRIM GRID LINES AGAINST LOFT SOLID
# ================================================================
loft_solid = loft.DuplicateBrep()

def trim_by_solid(curve, solid, tolerance, n_samples=200):
    dom = curve.Domain
    t0, t1 = float(dom.T0), float(dom.T1)
    ts = [t0 + (t1 - t0) * i / n_samples for i in range(n_samples + 1)]

    outside = []
    for t in ts:
        pt = curve.PointAt(t)
        try:
            outside.append(not solid.IsPointInside(pt, tolerance, False))
        except Exception:
            outside.append(True)

    result, seg_start = [], None
    for t, out in zip(ts, outside):
        if out and seg_start is None:
            seg_start = t
        elif not out and seg_start is not None:
            seg = curve.Trim(seg_start, t)
            if seg is not None:
                result.append(seg)
            seg_start = None
    if seg_start is not None:
        seg = curve.Trim(seg_start, t1)
        if seg is not None:
            result.append(seg)
    return result

trimmed = []
for crv in raw_lines:
    trimmed.extend(trim_by_solid(crv, loft_solid, tol))

# ================================================================
# GROUP 5 — EXTRUDE EACH SEGMENT INTO A RECTANGULAR BEAM
#
# Cross-section orientation:
#   horizontal beams → width perpendicular in XY plane, height in Z
#   vertical columns → width in X, height in Y
#
# Method: build a Box whose plane X-axis runs along the beam,
#         Y-axis is the horizontal-perpendicular (ax),
#         Z-axis (normal) = d × ax.
#         Origin is offset by -ax*(bw/2) - normal*(bh/2)
#         so the cross-section is centred on the line.
# ================================================================
def make_beam(crv, width, height):
    s = crv.PointAtStart
    e = crv.PointAtEnd
    d = e - s
    span = d.Length
    if span < 1e-6:
        return None
    d.Unitize()

    if abs(d.Z) > 0.9:               # vertical column
        ax = rg.Vector3d.XAxis
    else:                             # horizontal beam
        ax = rg.Vector3d.CrossProduct(rg.Vector3d.ZAxis, d)
        ax.Unitize()

    normal = rg.Vector3d.CrossProduct(d, ax)
    normal.Unitize()

    origin = s - ax * (width * 0.5) - normal * (height * 0.5)
    plane  = rg.Plane(origin, d, ax)
    box    = rg.Box(plane,
                    rg.Interval(0, span),
                    rg.Interval(0, width),
                    rg.Interval(0, height))
    return box.ToBrep() if box.IsValid else None

beams = []
for seg in trimmed:
    b_geo = make_beam(seg, bw, bh)
    if b_geo is not None:
        beams.append(b_geo)

# ================================================================
# GROUP 6 — OUTPUTS
# ================================================================
a = trimmed    # trimmed grid lines (curves)
b = beams      # rectangular beam extrusions (Breps)
