# Erosion Simulation

A Houdini heightfield network that simulates terrain erosion: base noise
generates a height field, which is distorted and layered, then run through
Houdini's hydraulic erosion and terracing solvers with a flow-field pass to
visualize where water would carve the terrain over time.

Node graph (all stock Houdini heightfield SOPs): `heightfield_noise` →
`heightfield_distort` / `heightfield_distortbylayer` → `heightfield_layer` →
`heightfield_erode` → `heightfield_terrace` → `heightfield_flowfield` →
`heightfield_visualize`, with mask nodes controlling where erosion is applied.

Pairs well with [`Analysis/slope`](../slope) and
[`Analysis/rainwater_flow`](../rainwater_flow) — three different ways of
evaluating how water and material move across a site.

## File

| File | What it does |
|------|--------------|
| [`erosion_simulation.hip`](erosion_simulation.hip) | Houdini scene: heightfield erosion simulation. |

## Usage

1. Open in Houdini.
2. Adjust the noise parameters on `heightfield_noise1` to set the base terrain.
3. Tune the `heightfield_erode1` and `heightfield_terrace1` parameters to
   control erosion strength and terracing.
4. Use `heightfield_visualize1` / `heightfield_flowfield1` to preview the
   result.

## Software

- SideFX Houdini
