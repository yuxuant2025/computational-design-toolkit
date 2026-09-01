# Computational Design Toolkit

A curated collection of scripts by **Yuxuan Tu** for architecture and design
work — Grasshopper / GhPython definitions for Rhino, plus a toolkit of
automation scripts for Adobe Illustrator.

The collection is split into three parts:

### [`Geometry/`](Geometry) — project geometry systems

Resolved, often complex geometry from real projects: a lofted lattice with a
beam grid, circle-packed floors, dome panelization. Each entry is
self-contained, with the source definition and a README documenting its intended
use — plus, where available, extracted component code, a canvas snapshot, and
project renders that used its output.

### [`Modeling_Help/`](Modeling_Help) — reusable modeling aids

Small, single-purpose Grasshopper definitions for everyday modeling tasks —
perforation, ramps, contours, fillets, tweens, diagrids. Project-agnostic, meant
to be copied out and adapted. Kept loose: a short README per topic, no
screenshots.

### [`Illustrator/`](Illustrator) — Adobe Illustrator automation

ExtendScript (`.jsx`) utilities for repetitive drawing and layout tasks in Adobe
Illustrator. A different tool and language from the Grasshopper work.

## Index

### Geometry

| Script | Description |
|--------|-------------|
| [Lofting Lattice With Grid](Geometry/Lofting_Lattice_With_Grid) | Stacked lofted slabs cut from a surface, plus a 3D beam grid trimmed to a lofted solid. |
| [Circle Packing](Geometry/Circle_Packing) | Dense packing of non-overlapping circles inside a boundary, used to generate a floor pattern. |
| [Dome Panelization](Geometry/Dome_Panelization) | Panelizes a dome/spherical surface with circular panels placed on points distributed across it. |

### Modeling Help

| Topic | Description |
|-------|-------------|
| [tween](Modeling_Help/tween) | Interpolate in-between shapes between two curves / sections. |
| [contour](Modeling_Help/contour) | Slice geometry into evenly spaced contour / section curves. |
| [ramp](Modeling_Help/ramp) | Ramps with a landing, and spiral (helical) ramps. |
| [perforation](Modeling_Help/perforation) | Distribute openings across a panel, sized by an attractor. |
| [diagrid](Modeling_Help/diagrid) | Diagonal structural grid over a roof surface. |
| [fillet](Modeling_Help/fillet) | Offset a curve and round its corners. |

### Illustrator

_Being organized; index to follow._

## Software

- Rhino + Grasshopper (Rhino 7 or later)
- RhinoCommon / `Rhino.Geometry` (via GhPython)
- Adobe Illustrator (ExtendScript / `.jsx`)
