// stroke-to-fill.jsx
// For every path in the active document: move the stroke color into the fill,
// clear the stroke, and set the object opacity to 80%.

if (app.documents.length > 0 && app.activeDocument.pathItems.length > 0) {
    doc = app.activeDocument;
    for (var i = 0; i < doc.pathItems.length; i++) {
        pathRef = doc.pathItems[i];
        pathRef.filled = true;
        pathRef.stroked = true;
        //swatchIndex = Math.round( Math.random() * ( doc.swatches.length - 1 ));
        pathRef.fillColor = pathRef.strokeColor;
        pathRef.strokeColor = NoColor;
        pathRef.opacity = 80;
    }
}
