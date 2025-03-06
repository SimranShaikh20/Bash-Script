import threading

# Sample Sudoku puzzle (valid solution)
sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 3, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Shared list to store validation results (1 = valid, 0 = invalid)
validity = [0] * 11

# Function to check if a list contains digits 1-9 exactly once
def is_valid(lst):
    return sorted(lst) == list(range(1, 10))

# Thread function to validate rows
def check_rows():
    for row in sudoku:
        if not is_valid(row):
            return  # Invalid row found
    validity[0] = 1  # Mark rows as valid

# Thread function to validate columns
def check_columns():
    for col in zip(*sudoku):
        if not is_valid(col):
            return  # Invalid column found
    validity[1] = 1  # Mark columns as valid

# Thread function to validate a 3x3 subgrid
def check_subgrid(start_row, start_col, index):
    subgrid = [
        sudoku[r][c] for r in range(start_row, start_row + 3)
        for c in range(start_col, start_col + 3)
    ]
    if is_valid(subgrid):
        validity[index] = 1  # Mark subgrid as valid

# Create and start threads
threads = []

# Row and column validation threads
t1 = threading.Thread(target=check_rows)
t2 = threading.Thread(target=check_columns)
threads.extend([t1, t2])

# Subgrid validation threads (9 subgrids)
index = 2  # Index in validity list
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        t = threading.Thread(target=check_subgrid, args=(i, j, index))
        threads.append(t)
        index += 1

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Final validation
if all(validity):
    print("The Sudoku solution is VALID!")
else:
    print("The Sudoku solution is INVALID!")
