def isValidSudoku(board) -> bool:
    for row in board:
        if not check_list(row):
            return False

    for col in range(len(board[0])):
        list_col = []
        for i in range(len(board)):
            list_col.append(board[i][col])
        if not check_list(list_col):
            return False

    for i in range(0, len(board), 3):
        k = 0
        while k < len(board):
            j = i
            three_by_three = []
            while j - i != 3:
                l = k
                while l - k != 3:
                    three_by_three.append(board[j][l])
                    l += 1
                j += 1
            if not check_list(three_by_three):
                return False
            k += 3
    return True


def check_list(list):
    number_set = set()
    for number in list:
        if number != "." and number in number_set:
            return False
        else:
            number_set.add(number)
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
