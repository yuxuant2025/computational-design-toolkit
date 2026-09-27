# Elefront Bake Attributes

Bakes geometry from Grasshopper into Rhino with attached user-text attributes
(via the Elefront plugin), so parametric data travels with the geometry into
downstream BIM tools instead of being lost on bake.

## File

| File | What it does |
|------|--------------|
| [`elefront_bake_attributes.gh`](elefront_bake_attributes.gh) | Bakes geometry with Elefront, attaching key/value attributes to each object. |

## Usage

1. Open in Grasshopper (Rhino 7+) with the **Elefront** plugin installed.
2. Reference the geometry and the attribute key/value pairs to attach.
3. Bake — the resulting Rhino objects carry the attributes as user text.

## Software

- Rhino + Grasshopper
- Elefront (plugin, required)
