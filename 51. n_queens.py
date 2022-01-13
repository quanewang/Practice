def n_queens(n):
    solutions = []
    valid_squares = set()
    valid_squares.copy()
    board = []
    for i in range(0, n):
        board.append("." * n)
        for j in range(n):
            valid_squares.add((i, j))

    for j in range(len(board)):
        copy = board.copy()
        valid_copy = valid_squares.copy()
        solution = set()
        solutions.extend(try_square(0, j, copy, valid_copy, solution))
    return solutions


def try_square(i, j, copy, valid_squares, solution, count=1):
    solutions = []
    validate_squares(i, j, copy, valid_squares)
    solution.add((i, j))
    if len(solution) == len(copy):
        copied = copy.copy()
        for (i, j) in solution:
            temp = copied[i][0:j]
            copied[i] = temp + "Q" + copied[i][j + 1:len(copied[i])]
        solutions.append(copied)
        return solutions
    for j in range(len(copy)):
        if (i + 1, j) in valid_squares:
            solutions.extend(try_square(i + 1, j, copy, valid_squares.copy(), solution.copy(), count + 1))

    return solutions


def validate_squares(i, j, copy, valid_squares):
    if not valid_squares:
        return
    for row in range(len(copy)):
        if (row, j) in valid_squares:
            valid_squares.remove((row, j))

    for col in range(len(copy)):
        if (i, col) in valid_squares:
            valid_squares.remove((i, col))

    k = i + 1
    l = j + 1
    while k < len(copy) and l < len(copy):
        if (k, l) in valid_squares:
            valid_squares.remove((k, l))
        k += 1
        l += 1

    k = i + 1
    l = j - 1
    while k < len(copy) and l >= 0:
        if (k, l) in valid_squares:
            valid_squares.remove((k, l))
        k += 1
        l -= 1
    return


print(n_queens(4))
print(n_queens(1))
print(n_queens(5))
