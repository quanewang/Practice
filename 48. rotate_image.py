def rotate_image(matrix):
    transpose_matrix(matrix)
    left = 0
    right = len(matrix) - 1
    while left < right:
        for i in range(len(matrix)):
            temp = matrix[i][left]
            matrix[i][left] = matrix[i][right]
            matrix[i][right] = temp
        left += 1
        right -= 1


def transpose_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_image(matrix)
print(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate_image(matrix)
print(matrix)
