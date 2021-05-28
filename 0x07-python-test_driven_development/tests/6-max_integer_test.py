#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        md = __import__('6-max_integer').__doc__
        self.assertTrue(len(md) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        fdstr = max_integer.__doc__
        self.assertTrue(len(fdstr) > 1)

    def test_one_element(self):
        """Tests for only number"""
        l = [12]
        self.assertEqual(max_integer(l), 12)

    def test_positive_end(self):
        """Tests for max at end"""
        l = [40, 1, 43, 61, 12, 430]
        self.assertEqual(max_integer(l), 430)

    def test_positive_middle(self):
        """Tests for max in middle"""
        l = [7, 11, 3, 190, 81, 40]
        self.assertEqual(max_integer(l), 190)

    def test_positive_beginning(self):
        """Tests for max at beginning"""
        l = [431, 16, 28, 321, 112, 88]
        self.assertEqual(max_integer(l), 431)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        l = [122, 54, 2, -20, 3, 10]
        self.assertEqual(max_integer(l), 122)

    def test_negative_numbers(self):
        """ Tests for list of negative numbers"""
        l = [-12, -1, -56, -80, -45, -10]
        self.assertEqual(max_integer(l), -1)

    def test_empty_list(self):
        """Tests for empty list"""
        l = []
        self.assertIsNone(max_integer(l))

    def test_no_args(self):
        """Tests for no arguments"""
        self.assertIsNone(max_integer())

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [10, 1, "Holberton", 12, 4]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
