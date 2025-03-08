# Sudoku Validator (Multithreaded)

## Problem Statement
A Sudoku puzzle uses a 9x9 grid in which each **row**, **column**, and **3x3 subgrid** must contain all digits **1-9 exactly once**. This project consists of designing a **multithreaded application** that verifies whether a given Sudoku solution is valid.

## Solution Approach
We use **multithreading** to validate the Sudoku solution efficiently. The validation is divided into three checks:
1. **Row validation** - Ensures all rows contain numbers 1-9.
2. **Column validation** - Ensures all columns contain numbers 1-9.
3. **3x3 Subgrid validation** - Ensures each 3x3 subgrid contains numbers 1-9.

A total of **11 threads** are created:
- **1 thread** to check all rows
- **1 thread** to check all columns
- **9 threads** to check each 3x3 subgrid

Each thread updates a shared `valid` list, which the main thread checks to determine if the solution is valid.

## Code Implementation
```python
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
        if sorted(row) != list(range(1, 10)):
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
```

## How to Run
1. Ensure you have **Python 3.x** installed.
2. Copy the above code into a file, e.g., `sudoku_validator.py`.
3. Run the script using:
   ```sh
   python sudoku_validator.py
   ```

## Expected Output
For a valid Sudoku solution, the output will be:
```
The Sudoku solution is valid!
```
For an invalid Sudoku solution, the output will be:
```
The Sudoku solution is invalid!
```

## Features
✅ **Uses Multithreading** for efficient Sudoku validation.  
✅ **Checks rows, columns, and 3x3 subgrids separately**.  
✅ **Fast and efficient** - runs **11 threads in parallel**.  
✅ **Easy to modify** for different Sudoku puzzles.  

## Future Improvements
🔹 Allow user input for Sudoku puzzles.  
🔹 Validate incomplete puzzles.  
🔹 Use multiprocessing for better performance.  

## License
This project is open-source and available under the **MIT License**.
