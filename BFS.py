# board = [1, 3, 0, 2]

# In the first row, the queen is placed in column 1.
# In the second row, the queen is placed in column 3.
# In the third row, the queen is placed in column 0.
# In the fourth row, the queen is placed in column 2.
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_board(board):
    n = len(board)
    for i in range(n):
        row_str = ""
        for j in range(n):
            if board[i] == j:
                row_str += "Q "
            else:
                row_str += ". "
        print(row_str)
    print('\n')


def bfs_nqueens(n):
    queue = []
    queue.append([])
    while len(queue) > 0:
        board = queue.pop(0)
        if len(board) == n:
            print_board(board)
        else:
            for i in range(n):
                if is_safe(board, len(board), i):
                    new_board = board + [i]
                    queue.append(new_board)


# Example usage for solving 4-queens problem
bfs_nqueens(4)
