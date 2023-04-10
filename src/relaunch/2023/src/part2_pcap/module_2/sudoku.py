from typing import List
from pprint import pprint

table: List[str] = []


def validate_input_row(row, row_len:int = 9, min_val:int = 1, max_val:int = 9) -> bool:
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
    for line in range(9):
        valid_row = False
        while not valid_row:
            row = input(f"Enter table row [{line}] (valid: 9 12234numbers without separator): ")
            valid_row = validate_input_row(row)
            if valid_row:
                table.append(row)


def init_table(data: str, row_len: int = 9) -> bool:
    if len(data) != 81:
        return False
    for row_idx in range(9):
        row = data[row_idx*row_len:row_idx*row_len+9]
        valid_row = validate_input_row(row)
        if valid_row:
            table.append(row)
        else:
            return False
    return True


def clean_table():
    global table
    for row in table:
        del row
    table = []


def check_table(tab: list) -> bool:
    res = [(len(set(row)) == 9) for row in tab]
    try:
        res.index(False)
    except ValueError:
        return True
    return False


def transpose_table(tab: list) -> list:
    res = []
    for row in zip(*tab):
        res.append(''.join(row))
    return res


def get_table_cell(tab: list, x: int = 0, y: int = 0) -> list:
    return [''.join([row[(x*3):(x*3)+3] for row in tab[(y*3):(y*3)+3]])]


def check_cells(tab: list) -> bool:
    for cell_x in range(3):
        for cell_y in range(3):
            if not check_table(get_table_cell(tab, cell_x, cell_y)):
                return False
    return True


def validate_table(tab: list) -> bool:
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
