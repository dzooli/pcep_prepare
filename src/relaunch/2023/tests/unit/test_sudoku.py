from unittest import TestCase
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..\\..\\src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../src"))

from part2_pcap.module_2 import sudoku


class TestSudoku(TestCase):
    VALID_TABLE_INPUT = '123456789987654321123123123123123123123122342343423455433453452423434598798798798'
    SHORT_TABLE_INPUT = '12345678998765432112312312312312312312312234234342345543345345242343459879879879'
    INVALID_TABLE_INPUT = 'a23456789987654321123123123123123123123122342343423455433453452423434598798798798'

    def setUp(self) -> None:
        sudoku.clean_table(sudoku.table)

    def test_validate_input_row_ok(self):
        res = sudoku.validate_input_row('123456789')
        self.assertEqual(res, True, "Valid row marked as invalid!")

    def test_validate_input_row_notok(self):
        res = sudoku.validate_input_row('a23456789')
        self.assertEqual(res, False, "Invalid row marked as valid!")

    def test_validate_input_row_short(self):
        self.assertFalse(sudoku.validate_input_row('1234'))

    def test_init_table_ok(self):
        self.assertTrue(sudoku.init_table(self.VALID_TABLE_INPUT))
        self.assertTrue(len(sudoku.table), "Table is not initialized!")

    def test_init_table_too_short(self):
        self.assertFalse(sudoku.init_table(self.SHORT_TABLE_INPUT), "Table is initialized with short input")

    def test_init_table_notok(self):
        self.assertFalse(sudoku.init_table(
            self.INVALID_TABLE_INPUT))
        self.assertEqual(len(sudoku.table), 0, "Table is initialized with invalid data!")

    def test_clean_table(self):
        sudoku.init_table(self.VALID_TABLE_INPUT)
        sudoku.clean_table(sudoku.table)
        self.assertEqual(len(sudoku.table), 0, "Table is not clean")

    def test_get_table_cell(self):
        sudoku.init_table(
            self.VALID_TABLE_INPUT)
        cell1 = sudoku.get_table_cell(sudoku.table, 0, 0)
        self.assertEqual(cell1, ['123987123'], "Table cell retrieves and invalid cell")

