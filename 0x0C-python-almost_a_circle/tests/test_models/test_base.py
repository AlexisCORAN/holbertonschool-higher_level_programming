#!/usr/bin/python3
"""
Unittest of Base class
"""
import unittest
from models import base


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation"""
    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(base.Base.__doc__) >= 1)
   
