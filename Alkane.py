__author__ = 'rheintze'

from chemspipy import *
from cactusAPI import get_csid
from Carbon import Carbon
from Exceptions import *
class Alkane:
    """
    A class used to implement an organic compound.
    """

    chain = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane',
             'undecane','dodecane','tridecane','tetradecane','pentadecane')
    substituent = ('methyl','ethyl','propyl','butyl','pentyl')

    def __init__(self, matrix):
        self.carbons = []
        self.head = None
        self.initGraph(matrix)
        if self.head == None:
            raise EmptyAlkaneError()
        isConnected, hasCycles = self.isConnectedHasCycles()
        if not isConnected:
            raise AlkaneNotConnectedError()
        if hasCycles:
            raise CyclicAlkaneError()
#        self.longestChain = self.getLongestChain()
    
    #Initialize graph and carbon list based on carbon matrix    
    def initGraph(self, graphicMatrix):
        width = len(graphicMatrix)
        height = len(graphicMatrix[0])
        #Dict of position tuples to carbon objects
        #Used to remember where we have already found carbons 
        carbonDict = {}
        for col_index in range(0, width):
            for row_index in range(0, height):
                #Skip empty spaces
                if not graphicMatrix[col_index][row_index]:
                    continue
                thisCarbon = Carbon()
                self.carbons.append(thisCarbon)
                #Remember that this carbon is at this location for when we make our double-links
                carbonDict[(row_index, col_index)] = thisCarbon
                otherCarbon = None
                #Have we found our first carbon? 
                if self.head == None:
                    self.head = thisCarbon
                
                #Is there a valid, occupied space to the left?
                if col_index>0 and graphicMatrix[col_index-1][row_index]:
                    #Remember which carbon was in this space
                    otherCarbon = carbonDict[(col_index-1,row_index)]
                    #Create double-link between our Carbon nodes
                    thisCarbon.west = otherCarbon
                    otherCarbon.east = thisCarbon
                        
                #Is there a valid, occupied space to the top?
                if row_index and graphicMatrix[col_index][row_index-1]:
                    #Remember which carbon was in this space
                    otherCarbon = carbonDict[(col_index,row_index-1)]
                    #Create double-link between our Carbon nodes
                    thisCarbon.north = otherCarbon
                    otherCarbon.south = thisCarbon
                    
    #Check if carbons are connected and graph has no cycles
    def isConnectedHasCycles(self):
        isConnected = True
        hasCycles = False
        totalSet = set(self.carbons)
        connectedSet = set()
        try:
            self.addCarbonsToSet(head, connectedSet)
        except:
            hasCycles = True
        if totalSet != connectedSet:
            isConnected = false
        return (isConnected, hasCycles)
        
    def addCarbonsToSet(self, carbon, carbonSet, ignoreDirection=None):
        if carbon in carbonSet:
            raise CyclicAlkeneError()
        else:
            carbonSet.append(carbon)
        if carbon.north and ignoreDirect != 'north':
            self.addCarbonsToSet(carbon.north, carbonSet, 'south')
        if carbon.east and ignoreDirect != 'east':
            self.addCarbonsToSet(carbon.north, carbonSet, 'west')
        if carbon.south and ignoreDirect != 'south':
            self.addCarbonsToSet(carbon.north, carbonSet, 'north')
        if carbon.west and ignoreDirect != 'west':
            self.addCarbonsToSet(carbon.north, carbonSet, 'east')

#    def __init__(self, query):  #query will generally be in smiles or inchi
#        self.query = query
#        self.compound_maybe = Compound(get_csid(query))  #uses cactus search to find csid & constructs compound with it
#
#        pass

if __name__ == '__main__':
    #testing
    a = Alkane('C')                 #C Methane
    b = Alkane('CC(C)CC')           #CC(C)CC 2-Methylbutane
    c = Alkane('CC(C)(C)C')         #CC(C)(C)C 2,2-Dimethylpropane

    print(a.compound_maybe.smiles) #a
    print(a.compound_maybe.iupac)
    print(b.compound_maybe.smiles) #b
    print(b.compound_maybe.iupac)
    print(c.compound_maybe.smiles) #c
    print(c.compound_maybe.iupac)
    pass