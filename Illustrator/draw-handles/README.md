# Draw Handles

> **Third-party script.** Written by **Nihiltres**, not by the repo author.
> Included here as a collected utility, with the original attribution header
> preserved.

For every selected path, draws a straight line segment from each anchor point
out to each of its non-trivial Bézier handles (`leftDirection` / `rightDirection`).
Useful for illustrating or measuring the control-handle geometry of a curve.

- Recurses into compound paths.
- Flattens groups and layers in the selection to any depth.
- Skips handles that sit exactly on their anchor (trivial handles).
- New handle lines are added as plain stroked paths in the active document.

## File

| File | What it does |
|------|--------------|
| [`DrawHandles.jsx`](DrawHandles.jsx) | ExtendScript. Operates on the current selection. |

## Usage

1. Select one or more paths (groups / compound paths are fine).
2. **File → Scripts → Other Script…** and choose `DrawHandles.jsx`.

## Requirements

- Adobe Illustrator (ExtendScript / `.jsx`)
