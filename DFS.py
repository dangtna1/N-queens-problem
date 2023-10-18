def is_safe(board, row, col, N):
    # Check for attacks from the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for attacks from the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for attacks from the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N, result):
    if col >= N:
        temp = []
        for row in board:
            temp.append("".join(['Q' if i == 1 else '.' for i in row]))
        result.append(temp)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, result) or res
            board[i][col] = 0

    return res


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    if not solve_n_queens_util(board, 0, N, result):
        return []

    return result


# Example usage:
N = 4
solutions = solve_n_queens(N)
if solutions:
    for solution in solutions:
        for row in solution:
            print(row)
        print()
else:
    print("No solution exists for N = ", N)
