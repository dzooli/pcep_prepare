from behave import Given, When, Then
from part2_pcap.module_2 import sudoku


@Given("Table input from the user")
def table_input(context):
    sudoku.input_table()


@when(u'I retrieve the table from the module')
def step_impl(context):
    context.row_count = len(sudoku.table)
    context.sudoku_table = sudoku.table


@then(u'Row count is 9')
def step_impl(context):
    try:
        assert context.row_count == 9, "Invalid row count!"
    except KeyError:
        assert False, "No Sudoku table given!"


@Then(u'Each row contains 9 characters')
def valid_rows(context):
    for row in range(9):
        if len(context.sudoku_table[row]) != 9:
            raise ValueError('All rows must contain 9 characters')


@Then("Each row contains 9 numbers between {start:d} and {stop:d}")
def valid_chars_in_each_row(context, start: int, stop: int):
    for row in range(9):
        if len(context.sudoku_table[row]) != 9:
            raise ValueError('All rows must contain 9 characters')
        ch_idx = 0
        for ch in sudoku.table[row]:
            assert ch.isdigit(), f"Character in table[{row}][{ch_idx}] is not a number!"
            ch_int = int(ch)
            assert ch_int > 0 and ch_int <= 9, f"Number in table[{row}][{ch_idx}] is invalid!"
            ch_idx += 1
