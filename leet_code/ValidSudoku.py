import collections


def valid_sudoku(board):
    column = collections.defaultdict(set)
    row = collections.defaultdict(set)
    square = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            if board[r][c] in column[c] or board[r][c] in row[r] or board[r][c] in square[(r//3, c//3)]:
                return False

            column[c].add(board[r][c])
            row[r].add(board[r][c])
            square[(r//3, c//3)].add(board[r][c])

    return True




