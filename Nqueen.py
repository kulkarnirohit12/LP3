def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_nqueens(board, col, n):
    if col >= n:
        print_board(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = True
            res = solve_nqueens(board, col + 1, n) or res
            board[i][col] = False
    return res

n = int(input("Enter N: "))
board = [[False] * n for _ in range(n)]
solve_nqueens(board, 0, n)
