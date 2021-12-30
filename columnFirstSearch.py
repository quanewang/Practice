import sys


def columnFirstSearch(r):
    cols = {}
    t = [(r, 0)]
    cols.update({0: [r]})

    minCol = sys.maxsize
    maxCol = -sys.maxsize - 1

    while len(t) != 0:
        (node, col) = t.pop(0)
        vals = get(col, cols, node)
        cols.update({col: vals})
        
        if minCol > col:
            minCol = col
        if maxCol < col:
            maxCol = col

        if node.left is not None:
            leftCol = col - 1
            t.append((node.left, leftCol))

        if node.right is not None:
            rightCol = col + 1
            t.append((node.right, rightCol))

    path = []

    for i in range(minCol, maxCol + 1):
        path.extend(cols.get(i))

    return path


def get(i, dict, node):
    vals = dict.get(i)
    if vals is None:
        return [node]
    vals.append(node)
    return vals
