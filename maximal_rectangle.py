def maximal_rectangle(matrix):
    max_sum = 0
    sums_dict = {}
    for start_row in range(len(matrix)):
        for start_col in range(len(matrix[0])):
            for end_row in range(start_row, len(matrix)):
                for end_col in range(start_col, len(matrix[0])):
                    rectangle_sum = get_sum(matrix, start_row, start_col, end_row, end_col, sums_dict)
                    if rectangle_sum == (end_row + 1 - start_row) * (end_col + 1 - start_col):
                        if rectangle_sum > max_sum:
                            max_sum = rectangle_sum
    return max_sum


def get_sum(matrix, start_row, start_col, end_row, end_col, sums_dict):
    if (end_row, end_col) in sums_dict:
        rectangle_sum = sums_dict.get((end_row, end_col))
        if start_row - 1 >= 0 and start_col - 1 >= 0:
            rectangle_sum -= sums_dict.get((start_row - 1, end_col))
            rectangle_sum -= sums_dict.get((end_row, start_col - 1))
            rectangle_sum += sums_dict.get((start_row - 1, start_col - 1))
        elif start_row - 1 >= 0:
            rectangle_sum -= sums_dict.get((start_row - 1, end_col))
        elif start_col - 1 >= 0:
            rectangle_sum -= sums_dict.get((end_row, start_col - 1))
        return rectangle_sum
    matrix_sum = 0
    for row in range(end_row + 1):
        for col in range(end_col + 1):
            matrix_sum += int(matrix[row][col])
    sums_dict.update({(end_row, end_col): matrix_sum})
    return matrix_sum


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximal_rectangle(matrix))

matrix = [["0"]]
print(maximal_rectangle(matrix))

matrix = [["0", "0"], ["0", "0"]]
print(maximal_rectangle(matrix))
