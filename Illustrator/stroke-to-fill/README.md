# Stroke to Fill

Walks every path in the active Illustrator document and swaps the stroke onto
the fill: the fill color is set to the path's current stroke color, the stroke
is removed, and the object opacity is set to 80%.

Handy after tracing / generative work that comes in as stroked outlines when you
actually want filled shapes.

## File

| File | What it does |
|------|--------------|
| [`stroke-to-fill.jsx`](stroke-to-fill.jsx) | ExtendScript. Operates on all top-level `pathItems` in the active document. |

## Usage

1. Open a document with stroked paths.
2. **File → Scripts → Other Script…** and choose `stroke-to-fill.jsx`.

Runs on every path in the document (not just the selection), and only top-level
paths — not paths nested inside groups or compound paths.

## Known issue

`pathRef.strokeColor = NoColor;` references `NoColor` as a value, but it is a
constructor. To actually clear the stroke it should be:

```javascript
var noColor = new NoColor();
// ...
pathRef.stroked = false;
pathRef.strokeColor = noColor;
```

## Requirements

- Adobe Illustrator (ExtendScript / `.jsx`)
