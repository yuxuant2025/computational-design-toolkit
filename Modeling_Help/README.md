# Modeling Help

Small, single-purpose Grasshopper definitions for everyday modeling tasks —
the kind of thing you drop into your own file when you need it, not a finished
project.

This is the counterpart to [`Geometry/`](../Geometry), which holds resolved
geometry systems from real projects. Everything here is a **reusable modeling
aid**: generic, project-agnostic, and meant to be copied out and adapted.

Kept deliberately loose — a short README per topic, no canvas screenshots for
now.

## Index

| Topic | What it does |
|-------|--------------|
| [tween](tween) | Interpolate in-between shapes between two curves / sections. |
| [contour](contour) | Slice geometry into evenly spaced contour / section curves. |
| [ramp](ramp) | Ramps with a landing, and spiral (helical) ramps. |
| [perforation](perforation) | Distribute openings across a panel, sized by an attractor. |
| [diagrid](diagrid) | Diagonal structural grid over a roof surface. |
| [fillet](fillet) | Offset a curve and round its corners. |

## Software

- Rhino + Grasshopper (Rhino 7 or later)
