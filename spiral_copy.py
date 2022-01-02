def spiral_copy(arr):
    return get_spiral(arr, 0, len(arr) - 1, 0, len(arr[0]) - 1)


def get_spiral(arr, start_row, end_row, start_col, end_col):
    spiral = []
    if start_row == end_row or start_col == end_col:
        return spiral

    for i in range(start_col, end_col):
        spiral.append(arr[start_row][i])

    for i in range(start_row, end_row):
        spiral.append(arr[i][end_col])

    for i in range(end_col, start_col, -1):
        spiral.append(arr[end_row][i])

    for i in range(end_row, start_row, -1):
        spiral.append(arr[i][start_col])

    print(spiral)
    print((start_row, end_row, start_col, end_col))
    spiral.extend(get_spiral(arr, start_row + 1, end_row - 1, start_col + 1, end_col - 1))
    return spiral




print(spiral_copy([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]))
