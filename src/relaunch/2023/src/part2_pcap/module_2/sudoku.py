from typing import List

table: List[str] = []


def validate_input_row(row, row_len: int = 9, min_val: int = 1, max_val: int = 9) -> bool:
    """
    This function validates an input row for a Sudoku puzzle by checking that:

    - The length of the row matches row_len (default value of 9)
    - Each character in the row is a valid digit between min_val (default value of 1) and max_val (default value of 9)
    - If the above conditions are not satisfied then it returns False, else it returns True

     Arguments:
    - row: A list of characters representing a row in a Sudoku puzzle.
    - row_len: An integer representing the length of each row. Default value is 9.
    - min_val: An integer representing the minimum valid value for a digit. Default value is 1.
    - max_val: An integer representing the maximum valid value for a digit. Default value is 9.

     Returns:
    - A boolean value representing whether the row is valid or not.
    """
    if len(row) != row_len:
        return False
    for ch in row:
        try:
            le_min = int(ch) < min_val
            gt_max = int(ch) > max_val
            if ch.isdigit() is False or le_min or gt_max:
                return False
        except ValueError:
            return False
    return True


def input_table():
    """
    This function takes user input for each row of a Sudoku table

    Validates each row using the validate_input_row() function.
    If the row is valid, it is added to the table.
    If the row is not valid, the user is prompted to input the row again.

     Arguments:
    - None

     Returns:
    - None
    """
    for line in range(9):
        valid_row = False
        while not valid_row:
            row = input(f"Enter table row [{line}] (valid: 9 12234numbers without separator): ")
            valid_row = validate_input_row(row)
            if valid_row:
                table.append(row)


def init_table(data: str, row_len: int = 9) -> bool:
    """
    This function initializes a Sudoku table

    by taking in a string containing 81 characters and splitting it into 9 rows of 9 characters each.
    It then uses the validate_input_row() function to check the validity of each row,
    and if valid, adds it to the table.
    If any row is invalid, the function returns False, indicating that the table could not be initialized.

     Arguments:
    - data: A string containing 81 characters representing the initial state of the Sudoku table.
    - row_len: An integer representing the length of each row. Default value is 9.

     Returns:
    - A boolean value representing whether the Sudoku table was successfully initialized or not.
    """
    if len(data) != 81:
        return False
    for row_idx in range(9):
        row = data[row_idx * row_len:row_idx * row_len + 9]
        valid_row = validate_input_row(row)
        if valid_row:
            table.append(row)
        else:
            return False
    return True


def clean_table(tab: list = None) -> None:
    """
    This function clears the contents of a given list, allowing for a clean start.

    If no list is provided, the function will not take any actions.

     Arguments:
    - tab: A list that needs to be cleared. Default value is None.

     Returns:
    -
    """
    if tab:
        tab.clear()


def check_table(tab: list) -> bool:
    """
    This function checks whether a given Sudoku table is valid or not

    by checking that each row contains exactly one occurrence of the digits 1-9.
    It does this by converting each row to a set and checking that the length of the set is 9.
    If any row fails this check, the function returns False indicating that the table is invalid,
    else it returns True indicating that the table is valid.

     Arguments:
    - tab: A list of lists representing the Sudoku table.

     Returns:
    - A boolean value representing whether the Sudoku table is valid or not.
    """
    res = [(len(set(row)) == 9) for row in tab]
    try:
        res.index(False)
    except ValueError:
        return True
    return False


def transpose_table(tab: list) -> list:
    """
    This function transposes a given Sudoku table by swapping its rows and columns.

    It does this by using the Python built-in function zip() to transpose the table
    and then appending each row to a new list. The rows of the new transposed table are returned as a list of strings.

     Arguments:
    - tab: A list of lists representing the Sudoku table.

     Returns:
    - A list of strings representing the transposed table.
    """
    res = []
    for row in zip(*tab):
        res.append(''.join(row))
    return res


def get_table_cell(tab: list, x: int = 0, y: int = 0) -> list:
    """
    This function returns a list containing the contents of a 3x3 cell of a Sudoku table, given the coordinates of
    the cell.

    It does this by using list slicing to extract the 3 rows that make up the cell,
    and then using string slicing to extract the 3 digits from each row that make up the cell's columns.
    The cell's rows and columns are then joined together into a single string and returned as a list.

     Arguments:
    - tab: A list of lists representing the Sudoku table.
    - x: An integer representing the horizontal coordinate (column) of the top-left cell of the 3x3 cell. Default: 0.
    - y: An integer representing the vertical coordinate (row) of the top-left cell of the 3x3 cell. Default: 0.

     Returns:
    - A list of strings representing the contents of the 3x3 cell.
    """
    return [''.join([row[(x * 3):(x * 3) + 3] for row in tab[(y * 3):(y * 3) + 3]])]


def check_cells(tab: list) -> bool:
    """
    This function checks whether all 9 cells of a 9x9 Sudoku table are valid or not by checking each cell individually.

    It does this by iterating over each cell in the table by using two for loops,
    and then passing each cell to the check_table() function to determine whether it is a valid cell.
    If any cell is found to be invalid, the function returns False, indicating that the table is invalid,
    else it returns True, indicating that the table is valid.

     Arguments:
    - tab: A list of lists representing the Sudoku table.

     Returns:
    - A boolean value representing whether all of the cells in the Sudoku table are valid or not.
    """
    for cell_x in range(3):
        for cell_y in range(3):
            if not check_table(get_table_cell(tab, cell_x, cell_y)):
                return False
    return True


def validate_table(tab: list) -> bool:
    """
    This function validates whether a given Sudoku table is valid or not by checking that:

    - Each row contains exactly one occurrence of the digits 1-9 using the check_table() function
    - Each column contains exactly one occurrence of the digits 1-9 by transposing the given table using the
      transpose_table() function and checking each row using the check_table() function
    - Each 3x3 cell contains exactly one occurence of the digits 1-9 using the check_cells() function

    If none of the above checks fail, the function returns True indicating that the Sudoku table is valid,
    else it returns False indicating that the Sudoku table is invalid.

     Arguments:
    - tab: A list of lists representing the Sudoku table.

     Returns:
    - A boolean value indicating whether the Sudoku table is valid or not.
    """
    valid_by_rows = check_table(tab)
    transposed_table = transpose_table(tab)
    valid_by_cols = check_table(transposed_table)
    valid_by_cells = check_cells(tab)
    return valid_by_rows and valid_by_cols and valid_by_cells


def main():
    input_table()
    print(validate_table(table))


if __name__ == "__main__":
    main()
