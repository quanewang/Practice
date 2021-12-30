def shortestPath(grid, sr, sc, tr, tc):
    p = [(sr, sc, [])]

    while p:
        (i, j, path) = p.pop(0)
        if (i, j) == (tr, tc):
            path.append((i, j))
            return path

        newPath = path.copy()
        newPath.append((i, j))
        if get(grid, i + 1, j, path):
            p.append((i + 1, j, newPath))

        if get(grid, i - 1, j, path):
            p.append((i - 1, j, newPath))

        if get(grid, i, j + 1, path):
            p.append((i, j + 1, newPath))

        if get(grid, i, j - 1, path):
            p.append((i, j - 1, newPath))

    return []


def get(a, i, j, path):
    if 0 <= i < len(a) and 0 <= j < len(a[0]) and not (i, j) in path:
        return a[i][j]
    else:
        return 0

grid = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print(shortestPath(grid, sr, sc, tr, tc))