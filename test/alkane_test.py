# -*- coding: utf-8 -*-
__author__ = 'rheintze'

"""
Unit tests for alkane.py
"""


import unittest

from chemistry.alkane import *
from chemistry.chem_exceptions import *

class TestAlkane(unittest.TestCase):
    def setUp(self):
        self.test_int = 50
        self.test_string = '50'

    def test_alkane(self):
        """ Unit tests for the Alkane class """
        
        
        #Matrix for empty Alkane
        #F F F
        #F F F
        #F F F
        emptyMatrix = [[False,False,False],[False,False,False],[False,False,False],]
        self.assertRaises(EmptyAlkaneError, Alkane, emptyMatrix)
        
        #Matrix for disconnected Alkane
        #T T T
        #F F F
        #F F T
        disconnectedMatrix = [[True,False,False,],[True,False,False,],[True,False,True,],]
        self.assertRaises(AlkaneNotConnectedError, Alkane, disconnectedMatrix)
        
        #Matrix for large-loop Alkane
        #T T T
        #T F T
        #T T T
        largeLoopMatrix = [[True,True,True,],[True,False,True,],[True,True,True,],]
        self.assertRaises(CyclicAlkaneError, Alkane, largeLoopMatrix)
        
        #Matrix for small-loop Alkane
        #T T T
        #F T T
        #F F F
        smallLoopMatrix = [[True,True,True,],[False,True,True,],[False,False,False,],]
        self.assertRaises(CyclicAlkaneError, Alkane, smallLoopMatrix)
        
        #Valid Carbon matrix #1
        #T T T
        #F F F
        #F F F
        validMatrixOne = [[True,True,True],[False,False,False],[False,False,False],]
        try:
            Alkane(validMatrixOne)
        except Exception as error:
            self.fail("Valid Alkane constructor #1 threw Exception\n"+str(error))


if __name__ == '__main__':
    unittest.main()