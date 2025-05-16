#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([42]), 42)

    def test_multiple_elements(self):
        """Test with multiple elements"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_string_elements(self):
        """Test with string elements"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')

    def test_mixed_elements(self):
        """Test with mixed elements"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])