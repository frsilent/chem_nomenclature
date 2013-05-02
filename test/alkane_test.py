# -*- coding: utf-8 -*-
__author__ = 'rheintze'

"""
Unit tests for alkane.py
"""


import unittest

from chemistry.alkane import *

class TestAlkane(unittest.TestCase):
    def setUp(self):
        self.test_int = 50
        self.test_string = '50'

    def test_alkane(self):
        """ Unit tests for the Alkane class """
        self.assertRaises(TypeError, Alkane, 1.2)
        self.assertRaises(TypeError, Alkane, 'notadigit')
        self.assertEqual(Carbon(self.test_int).int, self.test_string)


if __name__ == '__main__':
    unittest.main()