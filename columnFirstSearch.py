def columnFirstSearch(r):
    cols = {}
    t = [(r, 0)]
    cols.update({0: [r]})
    while len(t) != 0:
        (node, col) = t.pop(0)

        if node.left is not None:
            leftCol = col - 1

            vals = get(leftCol, cols, node.left)
            cols.update({leftCol: vals})

            t.append((node.left, leftCol))

        if node.right is not None:
            rightCol = col + 1

            vals = get(rightCol, cols, node.right)
            cols.update({rightCol: vals})

            t.append((node.right, rightCol))

    sortedKeys = sorted(cols.keys())
    path = []

    for i in sortedKeys:
        path.extend(cols.get(i))

    return path


def get(i, dict, node):
    vals = dict.get(i)
    if vals is None:
        return [node]
    vals.append(node)
    return vals
