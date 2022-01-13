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
        solution = try_square(0, j, copy, valid_copy, solution)
        if len(solution) == n:
            for (i, j) in solution:
                temp = copy[i][0:j]
                copy[i] = temp + "Q" + copy[i][j + 1:len(copy[i])]
            solutions.append(copy)
    return solutions


def try_square(i, j, copy, valid_squares, solution, count=1):
    validate_squares(i, j, copy, valid_squares)
    solution.add((i, j))
    if len(solution) == len(copy) or not valid_squares:
        return solution
    for j in range(len(copy)):
        if (i + 1, j) in valid_squares:
            sol = try_square(i + 1, j, copy, valid_squares.copy(), solution.copy(), count + 1)
            if len(sol) == len(copy):
                return sol

    return set()


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
