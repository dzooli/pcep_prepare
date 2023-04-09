# Created by fabia at 4/9/2023
@manual
Feature: Read table from user
  The program reads the table from user

  Background: Table input
    Given Table input from the user

  Scenario: Table has 9 valid rows
    When I retrieve the table from the module
    Then Row count is 9
    And Each row contains 9 characters
    And Each row contains 9 numbers between 1 and 9
