def n_queens(n):
    solutions = []
    invalid_squares = []
    board = []
    for i in range(0, n):
        board.append("." * n)
    solution = set()
    solutions.extend(try_square(0, board, invalid_squares, solution))
    return solutions


def try_square(i, board, invalid_squares, solution):
    solutions = []
    if i == len(board):
        return solutions
    for j in range(len(board)):
        if validate(i, j, invalid_squares):
            valid_copy = invalid_squares.copy()
            valid_copy.append(generate_valid(i, j))
            a_solution = solution.copy()
            a_solution.add((i, j))
            if len(a_solution) == len(board):
                copied = board.copy()
                for (r, c) in a_solution:
                    temp = copied[r][0:c]
                    copied[r] = temp + "Q" + copied[r][c + 1:len(copied[r])]
                solutions.append(copied)
                return solutions
            solutions.extend(try_square(i + 1, board, valid_copy, a_solution))

    return solutions


def generate_valid(i, j):
    return i, j, j - i, i + j


def validate(i, j, invalid_squares):
    for (r, c, d1, d2) in invalid_squares:
        if not ((i, j) == (r, c) or (i != r and j != c and (j - i) != d1 and (i + j) != d2)):
            return False
    return True


print(n_queens(4))
print(n_queens(1))
print(n_queens(5))
