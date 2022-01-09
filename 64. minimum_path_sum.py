import sys


def minimum_path_sum(grid):
    start = grid[0][0]
    queue = [(0, 0, start)]
    min_sum = sys.maxsize
    sum_dict = {(0, 0): start}
    while queue:
        i, j, sum = queue.pop(0)
        print(i, j)
        if i == len(grid) - 1 and j == len(grid[i]) - 1:
            if sum < min_sum:
                min_sum = sum
        if sum_dict.get((i, j)) is None:
            sum_dict.update({(i, j): sum})
            if j + 1 < len(grid[i]):
                queue.append([i, j + 1, sum + grid[i][j + 1]])
            if i + 1 < len(grid):
                queue.append([i + 1, j, sum + grid[i + 1][j]])
        else:
            if sum_dict.get((i, j)) > sum:
                sum_dict.update({(i, j): sum})
            if j + 1 < len(grid[i]) and sum_dict.get((i, j)):
                queue.append([i, j + 1, sum + grid[i][j + 1]])
            if i + 1 < len(grid):
                queue.append([i + 1, j, sum + grid[i + 1][j]])

    return min_sum


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
