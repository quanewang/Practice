def minimum_path_sum(grid):
    m = len(grid)
    n = len(grid[0])
    copy = [[0] * n]
    for row in range(m - 1):
        copy.append([0] * n)

    copy[m - 1][n - 1] = grid[m - 1][n - 1]

    for i in range(m).__reversed__():
        j = n - 1
        while j >= 0:
            min_sum = grid[i][j]
            if i + 1 < m and j + 1 < n:
                min_sum += min(copy[i + 1][j], copy[i][j + 1])
            elif i + 1 < m:
                min_sum += copy[i + 1][j]
            elif j + 1 < n:
                min_sum += copy[i][j + 1]
            copy[i][j] = min_sum
            j -= 1
    return copy[0][0]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minimum_path_sum(grid))

grid = [[1, 2, 3], [4, 5, 6]]
print(minimum_path_sum(grid))

grid = [[7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5], [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
        [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8], [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
        [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4], [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
        [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4], [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
        [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3], [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
        [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7], [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]]
print(minimum_path_sum(grid))
