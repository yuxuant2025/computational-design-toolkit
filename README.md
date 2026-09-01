# Computational Design Toolkit

A curated collection of computational-design scripts by **Yuxuan Tu** — mostly
Grasshopper / GhPython definitions for Rhino, developed in the course of
professional architecture and design work.

Each entry is a self-contained script folder with the source definition and a
README documenting its intended use — plus, where available, extracted component
code, a canvas snapshot, and project renders that used its output.

## Index

| Category | Script | Description |
|----------|--------|-------------|
| Geometry | [Lofting Lattice With Grid](Geometry/Lofting_Lattice_With_Grid) | Stacked lofted slabs cut from a surface, plus a 3D beam grid trimmed to a lofted solid. |
| Geometry | [Circle Packing](Geometry/Circle_Packing) | Dense packing of non-overlapping circles inside a boundary, driving a perforated facade pattern. |

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
