import threading

# Define Sudoku Grid
sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Global list to store validation results
valid = [False] * 11

def check_row():
    """Checks if all rows contain digits 1-9 exactly once"""
    for row in sudoku:
        if sorted(row) != list(range(1, 10)):  # Must contain 1-9 exactly once
            return
    valid[0] = True

def check_column():
    """Checks if all columns contain digits 1-9 exactly once"""
    for col in range(9):
        column_values = [sudoku[row][col] for row in range(9)]
        if sorted(column_values) != list(range(1, 10)):
            return
    valid[1] = True

def check_subgrid(start_row, start_col, index):
    """Checks if a 3x3 subgrid contains digits 1-9 exactly once"""
    subgrid = []
    for i in range(3):
        for j in range(3):
            subgrid.append(sudoku[start_row + i][start_col + j])
    if sorted(subgrid) == list(range(1, 10)):
        valid[index] = True

def main():
    threads = []

    # Create thread for checking rows
    row_thread = threading.Thread(target=check_row)
    threads.append(row_thread)

    # Create thread for checking columns
    col_thread = threading.Thread(target=check_column)
    threads.append(col_thread)

    # Create threads for checking 3x3 subgrids
    index = 2  # Start storing subgrid results from valid[2]
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_thread = threading.Thread(target=check_subgrid, args=(i, j, index))
            threads.append(subgrid_thread)
            index += 1

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Check if all validations passed
    if all(valid):
        print("The Sudoku solution is valid!")
    else:
        print("The Sudoku solution is invalid!")

if __name__ == "__main__":
    main()
