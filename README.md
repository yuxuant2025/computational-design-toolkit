# Computational Design Toolkit

A curated collection of computational-design scripts by **Yuxuan Tu** — mostly
Grasshopper / GhPython definitions for Rhino, developed in the course of
professional architecture and design work.

Each entry is a self-contained script folder with the source definition,
extracted component code, a canvas snapshot, project renders that used its
output, and a README documenting its inputs, outputs, and intended use.

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
