#!/usr/bin/python3
"""
Test for console.py
"""
import console
import unittest


class test_console(unittest.TestCase):
    """
    doc doc
    """
    def test_documentation(self):
        self.assertIsNotNone(console.__doc__)
