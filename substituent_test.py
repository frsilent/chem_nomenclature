# -*- coding: utf-8 -*-
__author__ = 'rheintze'

"""
Unit tests for alkane.py
"""


import unittest

from substituent import *

class TestSubstituent(unittest.TestCase):
    def setUp(self):
        self.test_int = 50
        self.test_string = '50'

    def test_substituent(self):
        """ Unit tests for the Alkane class """
        self.assertRaises(TypeError, Substituent, 1.2)
        self.assertRaises(TypeError, Substituent, 'notadigit')
        self.assertEqual(Substituent(self.test_int).int, self.test_string)

if __name__ == '__main__':
    unittest.main()