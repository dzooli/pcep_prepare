from pprint import pprint
from behave import use_step_matcher, Then
from part2_pcap.module_2 import sudoku

use_step_matcher("parse")


@Then(u'Row count is 9')
def row_count(context):
    assert len(sudoku.table) == 9, "Invalid row count!"


@Then(u'Each row contains 9 characters')
def step_impl(context):
    for row in range(9):
        if len(sudoku.table[row]) != 9:
            raise ValueError('All rows must contain 9 characters')


@Then("Each row contains 9 numbers between {start:d} and {stop:d}")
def valid_chars_in_each_row(context, start: int, stop: int):
    for row in range(9):
        if len(sudoku.table[row]) != 9:
            raise ValueError('All rows must contain 9 characters')
        ch_idx = 0
        for ch in sudoku.table[row]:
            assert ch.isdigit(), f"Character in table[{row}][{ch_idx}] is not a number!"
            ch_int = int(ch)
            assert ch_int > 0 and ch_int <= 9, f"Number in table[{row}][{ch_idx}] is invalid!"
            ch_idx += 1


@Then("Table is {valid} Sudoku table")
def valid_invalid_table(context, valid):
    is_valid = sudoku.validate_table(sudoku.table)
    if valid == 'valid':
        assert is_valid, "Table is not valid but expected to be!"
    elif valid == 'invalid':
        assert not is_valid, "Table is valid but expected to be not valid!"
    else:
        assert False, f"Invalid keyword in the gherkin file: {valid}"
