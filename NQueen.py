def solve_n_queens(n):
    board = [[' - ' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check if the current position is safe for a queen

        # Check column
        for i in range(row):
            if board[i][col] == ' Q ':
                return False

        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == ' Q ':
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == ' Q ':
                return False
            i -= 1
            j += 1

        return True


    def backtrack(row):
        # Base case: If all queens are placed, add the solution
        if row == n:
            solutions.append([''.join(row) for row in board])
            return
        # Try placing the queen in each column of the current row
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = ' Q '  # Place the queen
                backtrack(row + 1)  # Move to the next row
                board[row][col] = ' - '  # Backtrack

    backtrack(0)
    return solutions



solutions = solve_n_queens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()
