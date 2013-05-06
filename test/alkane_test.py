# -*- coding: utf-8 -*-
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
        
        #Malformed substituent Carbon Matrix 
        #T T T T T T T T T
        #T F T F T F F F F
        #T F F T T T F F F
        malformedSubMatrix = [
            [True, True, True, True, True, True, True, True, True,],
            [True, False, True, False, True, False, False, False, False,],
            [True, False, False, True, True, True, False, False, False,],
        ]
        self.assertRaises(BranchingCarbonChainError, Alkane, malformedSubMatrix)
        
        #Typical valid Carbon Matrix 
        #F F T F F F T F F
        #T T T T T T T T T
        #T F T F T F F F F
        #T F F F T T F F F
        typicalValidMatrix = [
            [False, False, True, False, False, False, True, False, False,],
            [True, True, True, True, True, True, True, True, True,],
            [True, False, True, False, True, False, False, False, False,],
            [True, False, False, False, True, True, False, False, False,],
        ]
        
        
        
        

if __name__ == '__main__':
    unittest.main()