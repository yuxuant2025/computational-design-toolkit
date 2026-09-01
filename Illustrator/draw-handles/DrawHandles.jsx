// DrawHandles.jsx
// Adobe Illustrator script to draw line segments to each anchor point of every selected path from each of its (nontrivial) handles.
// Nihiltres

function drawAllAnchorHandles(item) {
    var i;
    switch (item.typename) {
        case "PathItem":
            for (i = 0; i < item.pathPoints.length; i++) {drawAnchorHandles(item.pathPoints[i]);}
            break;
        case "CompoundPathItem":
            for (i = 0; i < item.pathItems.length; i++) {drawAllAnchorHandles(item.pathItems[i]);}
            break;
        default: return;
    }
}

function drawAnchorHandles(point) {
    drawNontrivialLine(point.leftDirection, point.anchor);
    drawNontrivialLine(point.rightDirection, point.anchor);
}

function drawNontrivialLine(start, end) {
    if (start[0] == end[0] && start[1] == end[1]) {return;}
    var r = app.activeDocument.pathItems.add();
    r.stroked = true;
    r.setEntirePath([start, end]);
}

function flattenSelection(collection, depth) {
    depth = ((typeof depth == "number") && !isNaN(depth)) ? (depth < 0 ? Infinity : depth) : 0;
    var r = [], i, j, t;
    for (i = 0; i < collection.length; i++) {
        switch (collection[i].typename) {
            case "Layer":
            case "GroupItem":
                t = depth > 0 ? flattenSelection(collection[i].pageItems, depth - 1) : [collection[i]];
                for (j = 0; j < t.length; j++) {r.push(t[j]);}
                break;
            default: r.push(collection[i]);
        }
    }
    return r;
}

var i, o = flattenSelection(app.activeDocument.selection, Infinity);
for (i = 0; i < o.length; i++) {drawAllAnchorHandles(o[i]);}
