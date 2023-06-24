# Created by fabia at 4/11/2023
Feature: Validate table

  Background:
    Given An empty Sudoku table

  Scenario Outline: Table validation
    When I initialize the table with this <data>
    Then Row count is 9
    And Each row contains 9 characters
    And Each row contains 9 numbers between 1 and 9
    And Table is <validity> Sudoku table

    Examples: Tables
      | data | validity |
      | 295743861431865927876192543387459216612387495549216738763524189928671354154938672 | valid    |
      | 195743862431865927876192543387459216612387495549216738763524189928671354254938671 | invalid  |

