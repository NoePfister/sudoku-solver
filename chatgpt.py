def is_valid(board, row, col, num):
    # Check if the number is not repeated in the current row, column, and 3x3 sub-grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(board):
    # Find the first empty cell (represented by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try each number from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        # Undo the move
                        board[row][col] = 0
                return False
    print(board)
    return True

def count_backtracking_loops(board):
    count = 0

    def solve(board):
        nonlocal count
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            count += 1
                            if solve(board):
                                
                                return True
                            board[row][col] = 0
                    return False
        return True
    print(board)
    solve(board)
    return count

# Solvable Sudoku puzzle
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

loops = count_backtracking_loops(sudoku_puzzle)
print("Number of loops required:", loops)
