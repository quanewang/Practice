def maximal_rectangle(matrix):
    max_sum = 0
    sum_arr = []
    for row in range(len(matrix)):
        sum_arr.append([0] * len(matrix[0]))

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            populate_sum(matrix, sum_arr, row, col)

    for start_row in range(len(matrix)):
        for start_col in range(len(matrix[0])):
            for end_row in range(start_row, len(matrix)):
                for end_col in range(start_col, len(matrix[0])):
                    rectangle_sum = get_sum(matrix, start_row, start_col, end_row, end_col, sum_arr)
                    if rectangle_sum == (end_row + 1 - start_row) * (end_col + 1 - start_col):
                        if rectangle_sum > max_sum:
                            max_sum = rectangle_sum
    for row in sum_arr:
        print(row)
    return max_sum


def populate_sum(matrix, sum_arr, row, col):
    rectangle_sum = int(matrix[row][col])
    if row - 1 >= 0:
        rectangle_sum += sum_arr[row - 1][col]
    if col - 1 >= 0:
        rectangle_sum += sum_arr[row][col - 1]
    if row - 1 >= 0 and col - 1 >= 0:
        rectangle_sum -= sum_arr[row - 1][col - 1]
    sum_arr[row][col] = rectangle_sum
    return None


def get_sum(matrix, start_row, start_col, end_row, end_col, sum_arr):
    rectangle_sum = sum_arr[end_row][end_col]
    if start_row - 1 >= 0:
        rectangle_sum -= sum_arr[start_row - 1][end_col]
    if start_col - 1 >= 0:
        rectangle_sum -= sum_arr[end_row][start_col - 1]
    if start_row - 1 >= 0 and start_col - 1 >= 0:
        rectangle_sum += sum_arr[start_row - 1][start_col - 1]
    return rectangle_sum


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximal_rectangle(matrix))

matrix = [["0"]]
print(maximal_rectangle(matrix))

matrix = [["0", "0"], ["0", "0"]]
print(maximal_rectangle(matrix))

matrix = [["0", "1"]]
print(maximal_rectangle(matrix))

