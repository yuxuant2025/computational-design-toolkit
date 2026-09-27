# Analysis

Definitions that **measure and evaluate** a design rather than generate form —
environmental and spatial performance tools. Mostly Grasshopper, with one
Houdini exception.

Where [`Geometry/`](../Geometry) and [`Modeling_Help/`](../Modeling_Help) produce
geometry, the definitions here take geometry as input and return numbers, maps,
or diagrams: how much sun a surface gets, what can be seen from a point, how
steep a site is, and so on. Each result is meant to feed back into a design
decision.

## Index

| Topic | What it does |
|-------|--------------|
| [slope](slope) | Evaluate grade across a terrain surface; flag buildable / unbuildable zones. |
| [rainwater_flow](rainwater_flow) | Trace rainwater flow paths across a terrain surface. |
| [rockfall](rockfall) | Kangaroo physics drop simulation for rockfall-hazard studies on steep sites. |
| [erosion](erosion) | Houdini heightfield simulation of terrain erosion over time. |

## Planned

| Tool | What it measures |
|------|------------------|
| solar exposure | Sun-hours / incident radiation across a surface over a date range. |
| view analysis (isovist) | What is visible from a viewpoint — area, perimeter, openness. |

## Software

- Rhino + Grasshopper (Rhino 7 or later) — all topics except `erosion`
- `rockfall` additionally requires the Kangaroo physics plugin
- `erosion` requires SideFX Houdini instead of Rhino/Grasshopper
