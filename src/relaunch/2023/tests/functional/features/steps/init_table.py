from behave import When, Then, Given, use_step_matcher
from part2_pcap.module_2 import sudoku

use_step_matcher("parse")

@Given("Table input from the user")
def table_input(context):
    sudoku.input_table()



@Then("Sudoku table is empty")
@Given("Sudoku table is empty")
def table_is_empty(context):
    assert len(sudoku.table) == 0, "Table is not empty!"


@When("I initialize the table with this {data}")
def fill_table(context, data):
    sudoku.init_table(data)


@Given("An empty Sudoku table")
def cleanup_table(context):
    sudoku.clean_table()
