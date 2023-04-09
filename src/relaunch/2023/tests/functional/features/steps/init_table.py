from behave import When, Then, Given, use_step_matcher
from part2_pcap.module_2 import sudoku

use_step_matcher("parse")


@Then("Sudoku table is empty")
@given("Sudoku table is empty")
def table_is_empty(context):
    assert len(sudoku.table) == 0, "Table is not empty!"


@when("I initialize the table with this data")
def fill_table(context):
    sudoku.init_table(context.table[0]["data"])


@given("An empty Sudoku table")
def step_impl(context):
    sudoku.clean_table()
