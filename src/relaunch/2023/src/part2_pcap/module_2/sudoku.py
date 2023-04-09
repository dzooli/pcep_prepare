from typing import List

table: List[str] = []


def validate_row(row) -> bool:
    if len(row) != 9:
        return False
    for ch in row:
        try:
            le_zero = int(ch) <= 0
            gt_nine = int(ch) > 9
            if ch.isdigit() is False or le_zero or gt_nine:
                return False
        except ValueError:
            return False
    return True


def input_table():
    for line in range(9):
        valid_row = False
        while not valid_row:
            row = input(f"Enter a valid table row [{line}]: ")
            valid_row = validate_row(row)
            if valid_row:
                table.append(row)


def init_table(data: str, row_len: int = 9) -> bool:
    if len(data) != 81:
        return False
    for row_idx in range(9):
        row = data[row_idx*row_len:row_idx*row_len+9]
        valid_row = validate_row(row)
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


def main():
    print(f"Main function called in {__file__}")
    input_table()


if __name__ == "__main__":
    main()
