# Analysis

Grasshopper definitions that **measure and evaluate** a design rather than
generate form — environmental and spatial performance tools.

Where [`Geometry/`](../Geometry) and [`Modeling_Help/`](../Modeling_Help) produce
geometry, the definitions here take geometry as input and return numbers, maps,
or diagrams: how much sun a surface gets, what can be seen from a point, how
steep a site is, and so on. Each result is meant to feed back into a design
decision.

## Planned tools

| Tool | What it measures |
|------|------------------|
| solar exposure | Sun-hours / incident radiation across a surface over a date range. |
| view analysis (isovist) | What is visible from a viewpoint — area, perimeter, openness. |
| slope analysis | Grade across a terrain surface, with buildable / unbuildable zones. |

_Scripts to be added; index to follow._

## Software

- Rhino + Grasshopper (Rhino 7 or later)
- Environmental tools may additionally require a solar / weather plugin
  (e.g. Ladybug) — noted per script where used.
