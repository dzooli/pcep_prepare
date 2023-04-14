import os
import sys
import unittest
import pytest
from pytest import fixture

sys.path.append(os.path.join(os.path.dirname(__file__), "..\\..\\src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../src"))

from part2_pcap.module_3.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.st = Stack()

    def test_add_element(self):
        self.st.push(1)
        self.assertEqual(len(self.st), 1)

    def test_pop_element(self):
        self.st.push(2)
        elem = self.st.pop()
        self.assertEqual(len(self.st), 0)
        self.assertEqual(elem, 2)

    def test_add_more(self):
        self.st.push(1)
        self.st.push(2)
        self.assertEqual(len(self.st), 2)
        self.st.pop()
        self.assertEqual(len(self.st), 1)

    def test_len_valid(self):
        self.st.push(1)
        self.assertEqual(len(self.st), 1)
        self.st.pop()
        self.assertEqual(len(self.st), 0)

    def test_empty(self):
        self.st.push(1)
        self.assertFalse(self.st.empty())
        self.st.pop()
        self.assertTrue(self.st.empty())

    def test_top_eq_bottom_one_element(self):
        self.st.push(1)
        self.assertEqual(self.st.top(), self.st.bottom())

    def test_top_ne_bottom_two_elements(self):
        exp_top = 2
        exp_bottom = 1
        self.st.push(exp_bottom)
        self.st.push(exp_top)
        top_element = self.st.top()
        bottom_element = self.st.bottom()
        self.assertNotEqual(top_element, bottom_element)
        self.assertEqual(top_element, exp_top)
        self.assertEqual(bottom_element, exp_bottom)

    def test_pop_returns_none_on_empty(self):
        self.assertEqual(self.st.pop(), None)

    def test_empty_returns_true_uninitialized(self):
        self.assertEqual(self.st.empty(), True)
