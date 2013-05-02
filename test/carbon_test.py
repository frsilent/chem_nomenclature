# -*- coding: utf-8 -*-
__author__ = 'rheintze'

"""
Unit tests for carbon.py
"""


import unittest

from chemistry.carbon import *

class TestCarbon(unittest.TestCase):
    def setUp(self):
        pass
       
    def testGetOpposingDirections(self):
        self.assertEqual('north', Carbon.getOpposingDirection('south'), "The opposite of south was not north!")
        self.assertEqual('south', Carbon.getOpposingDirection('north'), "The opposite of north was not south!")
        self.assertEqual('east', Carbon.getOpposingDirection('west'), "The opposite of east was not west!")
        self.assertEqual('west', Carbon.getOpposingDirection('east'), "The opposite of west was not east!")
    
    def testGetDirections(self):
        directions = Carbon.directions()
        self.assertIn('north', directions, "North not in directions!")
        self.assertIn('south', directions, "South not in directions!")
        self.assertIn('east', directions, "East not in directions!")
        self.assertIn('west', directions, "West not in directions!")

    def testCarbon(self):
        carbon = Carbon(1,2)
        self.assertEqual(1, carbon.x, "X was wrong!")
        self.assertEqual(2, carbon.y, "Y was wrong!")
        for direction in Carbon.directions():
            self.assertEqual(getattr(carbon, direction), None, "Direciton: "+direction+" was not None!")

    def testGetDirectionTo(self):
        left_carbon = Carbon(1, 3)
        right_carbon = Carbon(2, 3)
        left_carbon.east = right_carbon
        right_carbon.west = left_carbon
        self.assertEqual(left_carbon.getDirectionTo(right_carbon), "east", "getDirectionTo returned the wrong direction!")
        
    def testBondTo(self):
        #     Top
        #Left Middle Right
        #     Bottom
        top = Carbon(1,0)
        middle = Carbon(1,1)
        right = Carbon(2,1)
        bottom = Carbon(1,2)
        left = Carbon(0,1)
        #Try all valid combinations to yield total success branch coverage
        try:
            top.bondTo(middle)
        except Exception as error:
            self.fail("bondTo from top to middle failed!\n"+str(error))
        
        top = Carbon(1,0)
        middle = Carbon(1,1)
        try:
            middle.bondTo(top)
        except Exception as error:
            self.fail("bondTo from middle to top failed!\n"+str(error))
        
        try:
            middle.bondTo(right)
        except Exception as error:
            self.fail("bondTo from middle to right failed!\n"+str(error))
            
        middle = Carbon(1,1)
        right = Carbon(2,1)
        
        try:
            right.bondTo(middle)
        except Exception as error:
            self.fail("bondTo from right to middle failed!\n"+str(error))
        
        #All combinations of outer carbons bonding together will yield total failure branch coverage
        outerCarbons = [top, right, bottom, left]
        for i in range(len(outerCarbons)):
            for j in range(i, len(outerCarbons)):
                self.assertRaises(CarbonsNotAdjacentError, outerCarbons[i].bondTo, outerCarbons[j])
        
    
    def testBondCarbons(self):
        #Create a set of connected carbons according to this map
        #  0 
        #1 2 3
        #  4
        carbons  = [
                     Carbon(1,0),
        Carbon(0,1), Carbon(1,1), Carbon(2,1),
                     Carbon(1,2),
        ]
        Carbon.bondCarbons(carbons)
        self.assertEqual(carbons[0].north,None)
        self.assertEqual(carbons[0].south,carbons[2])
        self.assertEqual(carbons[0].east,None)
        self.assertEqual(carbons[0].west,None)
        
        self.assertEqual(carbons[1].north,None)
        self.assertEqual(carbons[1].south,None)
        self.assertEqual(carbons[1].east,carbons[2])
        self.assertEqual(carbons[1].west,None)
        
        self.assertEqual(carbons[2].north,carbons[0])
        self.assertEqual(carbons[2].south,carbons[4])
        self.assertEqual(carbons[2].east,carbons[3])
        self.assertEqual(carbons[2].west,carbons[1])
        
        
        self.assertEqual(carbons[3].north,None)
        self.assertEqual(carbons[3].south,None)
        self.assertEqual(carbons[3].east,None)
        self.assertEqual(carbons[3].west,carbons[2])
        
        self.assertEqual(carbons[4].north,carbons[2])
        self.assertEqual(carbons[4].south,None)
        self.assertEqual(carbons[4].east,None)
        self.assertEqual(carbons[4].west,None)
        
        
    
    def testGetNumberOfBonds(self):
        #Create a set of connected carbons according to this map
        #  0 
        #1 2 3 4
        #5 6 7   8
        carbons  = [
                     Carbon(1,0),
        Carbon(0,1), Carbon(1,1), Carbon(2,1), Carbon(3,1),
        Carbon(0,2), Carbon(1,2), Carbon(2,2), Carbon(4,2)]
        expectedNumBonds = [1, 2, 4, 3, 1, 2, 3, 2, 0]
        #Bond all carbons together
        Carbon.bondCarbons(carbons)
        #Check number of bonds against expected number 
        for i in range(len(carbons)):
            self.assertEqual(carbons[i].getNumberOfBonds(), expectedNumBonds[i], "Expected "+ str(expectedNumBonds[i])+" bonds, found "+str(carbons[i].getNumberOfBonds)+" instead!")
        
        
    def testGetCarbonsInDirection(self):
        #A map of the carbons to test with
        #0 1
        #  2   
        #3 4 5 
        #      6
        carbons = [
            Carbon(0,0), Carbon(1,0),
                         Carbon(1,1),              
            Carbon(0,2), Carbon(1,2), Carbon(2,2), 
                                                   Carbon(3,3),                                                    
        ]
        #Bond the carbons together
        
        #Mapping of params to method (index in carbons, direction) to expected result 
        paramsToExpected = {
            (carbons[4], 'west') : [carbons[3]],
            (carbons[4], 'north') : [carbons[2],carbons[1],carbons[0]],
             
        }
        for (carbon,direction), expected in paramsToExpected:
            actual = carbon.getCarbonsInDirection(direction)
            if actual != expected:
                message = "Carbons didn't match!\n  Actual:\n"
                for act in actual:
                    message += str(act)+"\n"
                message += "  Expected:\n"
                for exp in expected:
                    message += str(exp)+"\n"
                self.fail(message)
        
        self.assertRaises(BranchingCarbonChainError, carbons[0].getCarbonsInDirection, 'east')
        
        
        
if __name__ == '__main__':
    unittest.main()