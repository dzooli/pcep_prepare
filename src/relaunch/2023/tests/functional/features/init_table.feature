# Created by fabia at 4/9/2023
Feature: Init a Sudoku table
  Sudoku table is initialized with strings

  Background: Clean table
    Given An empty Sudoku table

  Scenario: Initialize the table with valid data
    When I initialize the table with this data
      | data |
      | 123123123234234234345345345456456456567567567678678678789789789891891891912912912 |
    And I retrieve the table from the module
    Then Row count is 9
    And Each row contains 9 characters
    And Each row contains 9 numbers between 1 and 9

  Scenario: Initialize the table with invalid data
    When I initialize the table with this data
      | data |
      | a23123123234234234345345345456456456567567567678678678789789789891891891912912912 |
    Then Sudoku table is empty


