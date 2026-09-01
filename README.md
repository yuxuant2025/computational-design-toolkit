# Scripts

A collection of my computational-design scripts — mostly Grasshopper / GhPython
definitions for Rhino. Each script lives in its own folder with the source
files, a canvas snapshot, and a README describing its inputs and outputs.

## Index

| Category | Script | Description |
|----------|--------|-------------|
| Geometry | [Lofting Lattice With Grid](Geometry/Lofting_Lattice_With_Grid) | Stacked lofted slabs cut from a surface, plus a 3D beam grid trimmed to a lofted solid. |

## Layout

```
<Category>/
  <Script_Name>/
    README.md          description, inputs, outputs, usage
    *.gh               the Grasshopper definition
    *.py               extracted copies of the GhPython components
    images/            canvas snapshot and renders
```

## Software

- Rhino + Grasshopper (Rhino 7 or later)
- RhinoCommon / `Rhino.Geometry` (via GhPython)
