
def paths(n, i = 0, j = 0):
    p = 0

    if n == 0:
        return 0
    if (n - 1, n - 1) == (i, j):
        return 1
    if not i < n or not j <= i:
        return 0
    p += paths(n, i + 1, j)
    p += paths(n, i, j + 1)
    return p




def nonRecursivePaths(n):
    p = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = [[0] * n]
    for i in range(n - 1):
        a.append([0] * n)
    print(a)
    a[n - 1][n - 1] = 1
    print(a)
    for i in range(n).__reversed__():
        j = i
        while j >= 0:
            if 0 <= i + 1 < n:
                a[i][j] += a[i + 1][j]
            if j + 1 < n:
                a[i][j] += a[i][j + 1]
            j -= 1
    return a[0][0]




    return 0

print(paths(5, 0, 0))
print(nonRecursivePaths(5))
