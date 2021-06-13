#!/usr/bin/python3
"""
Unittest of Base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests for base class"""
    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_with_id_None(self):
        """Tests with id as None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_class_with_id(self):
        """Tests for 1 instance with id"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

