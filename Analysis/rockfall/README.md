# Rockfall Simulation

A Kangaroo physics simulation that drops a rigid body ("rock") onto a terrain /
site surface and lets it roll and bounce under gravity, tracing its path.
Used for rockfall-hazard studies on steep sites, and as a physical
(rather than vector-field) way to visualize the path loose material or water
would take down a slope.

_Description inferred from the filename (`kangaroo_drop rock.gh`) — correct
if this isn't quite what it does._

## File

| File | What it does |
|------|--------------|
| [`rockfall_simulation.gh`](rockfall_simulation.gh) | Kangaroo-driven rigid-body drop simulation over a terrain surface. |

## Usage

1. Open in Grasshopper (Rhino 7+) with the **Kangaroo** plugin installed.
2. Reference the terrain surface.
3. Set the drop point(s) and rock properties (size, bounce/friction), then run
   the Kangaroo solver.

## Software

- Rhino + Grasshopper
- Kangaroo (physics engine plugin)
