# -*- coding: utf-8 -*-
__author__ = 'rheintze'

"""
Unit tests for carbon.py
"""


import unittest

from carbon import *

class TestCarbon(unittest.TestCase):
    def setUp(self):
        self.test_int = 50
        self.test_string = '50'

    def test_carbon(self):
        """ Unit tests for the Carbon class """
        self.assertRaises(TypeError, Carbon, 1.2)
        self.assertRaises(TypeError, Carbon, 'notadigit')
        self.assertEqual(Carbon(self.test_int).int, self.test_string)

    def test_getCarbonsInDirection(self):
        self.assertEqual(False, None)

if __name__ == '__main__':
    unittest.main()