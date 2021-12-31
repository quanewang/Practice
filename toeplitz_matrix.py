def toeplitz_matrix(mat):
    for rows in range(len(mat) - 1):
        for cols in range(len(mat[rows]) - 1):
            if mat[rows][cols] != mat[rows + 1][cols + 1]:
                return False
    return True


print(toeplitz_matrix([[1, 2, 3, 4],
                       [5, 1, 2, 3],
                       [6, 5, 1, 2]]))

print(toeplitz_matrix([[1, 2, 3, 4],
                       [5, 1, 9, 3],
                       [6, 5, 1, 2]]))
