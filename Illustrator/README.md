# Illustrator

Automation scripts for **Adobe Illustrator** — a toolkit of small utilities for
repetitive drawing and layout tasks.

These are written in **ExtendScript** (Adobe's ECMAScript 3 dialect of
JavaScript), saved as `.jsx` files. They are unrelated to the Grasshopper work
in [`Geometry/`](../Geometry) and [`Modeling_Help/`](../Modeling_Help) — a
different tool and language, grouped here for convenience.

## Running a script

- **Illustrator → File → Scripts → Other Script…** and pick the `.jsx`, or
- drop the `.jsx` into Illustrator's `Presets/<locale>/Scripts/` folder so it
  appears directly in the **File → Scripts** menu, or
- run it from the ExtendScript Toolkit / VS Code with the ExtendScript Debugger.

## Index

| Script | Description | Author |
|--------|-------------|--------|
| [stroke-to-fill](stroke-to-fill) | Move each path's stroke color onto its fill, clear the stroke, set opacity to 80%. | Yuxuan Tu |
| [draw-handles](draw-handles) | Draw line segments from each anchor point to its Bézier handles, for selected paths. | Nihiltres (third-party) |

## Requirements

- Adobe Illustrator (ExtendScript / `.jsx` supported in all recent versions)
