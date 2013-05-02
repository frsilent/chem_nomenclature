__author__ = 'rheintze'

#from chemspipy import *
#from cactusAPI import get_csid
from chemistry.carbon import Carbon
from chemistry.substituent import Substituent
from chemistry.chem_exceptions import *
class Alkane:
    """
    A class used to implement an organic compound.
    """

    chain = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane',
             'undecane','dodecane','tridecane','tetradecane','pentadecane')
    substituent = ('methyl','ethyl','propyl','butyl','pentyl')
    
    MAX_CHAIN_LENGTH = len(chain)
    MAX_SUB_LENGTH = 4    
#    def __init__(self, longestChain):
#        self.carbons = longestChain[:]
#        self.longestChain = longestChain
#        self.head = longestChain[0]


    def __init__(self, matrix):
        self.carbons = [] #list of all nodes (carbons) in the graph (molecule)
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
#        self.name = self.getName()
#        #Reset head to first element in longest chain. This is the cannonical head.
#        self.head = self.longestChain[0]
#        try:
#            self.substituents = self._getSubstituents()
#        except BranchingCarbonChainError as error:
#            raise error

    #Throws BranchingCarbonChainError for malformed substituents

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
                thisCarbon = Carbon(col_index, row_index)
                self.carbons.append(thisCarbon)
                #Remember that this carbon is at this location for when we make our double-links
                carbonDict[(col_index, row_index)] = thisCarbon
                otherCarbon = None
                #Have we found our first carbon? 
                if self.head == None:
                    self.head = thisCarbon
                
                #Is there a valid, occupied space to the left?
                if col_index-1>0 and graphicMatrix[col_index-1][row_index]:
                    #Remember which carbon was in this space
                    otherCarbon = carbonDict[(col_index-1,row_index)]
                    #Create double-link between our Carbon nodes
                    thisCarbon.west = otherCarbon
                    otherCarbon.east = thisCarbon
                        
                #Is there a valid, occupied space to the top?
                if row_index-1>0 and graphicMatrix[col_index][row_index-1]:
                    #Remember which carbon was in this space
                    otherCarbon = carbonDict[(col_index,row_index-1)]
                    #Create double-link between our Carbon nodes
                    thisCarbon.north = otherCarbon
                    otherCarbon.south = thisCarbon

    #Check if carbons are connected and graph has no cycles
    def isConnectedHasCycles(self):
        isConnected = True
        hasCycles = False
        connectedSet = None
        totalSet = set(self.carbons)
        try:
            connectedSet = self.head.getConnectedSet()
        except CyclicAlkaneError:
            hasCycles = True
        if totalSet != connectedSet:
            isConnected = False
        return (isConnected, hasCycles)
    
    def getLongestChain(self):
        chains = []
        for carbon in self.carbons:
            chains.append(carbon.getLongestChain())
        #This is ugly but removes the problem of duplicate objects in getLongestChain
        #For refactoring find a way to only add carbons without visited flag
        return list(set(max(chains, key=len)))

    def getSubstituents(self):
        substituentCarbons = list(set(self.carbons) - set(self.longestChain)) #create list of carbons-longestchain
        for c in substituentCarbons: #TODO: Make function which creates a Substituent for each group of sub carbons
            pass

    def getName(self):
        basename = self.chain[len(self.getLongestChain())-1]

    def verify(self,guess):
        return guess == self.getName()
    
    def getCarbons(self):
        return self.carbons
    

#    def createRandomAlkane(self):
#        chain_length = random.randInt(6,Alkane.MAX_CHAIN_LENGTH)
#        max_sub_length = Alkane.MAX_CHAIN_LENGTH-chain_length
#        carbons = []
#        y = 5
#        for i in range(chain_length):
#            carbons.append(Carbon(2+i, y))
#        alkane = Alkane(carbons)
#        for i in range(chain_length):
#            if not random.randInt(0,y-1):
#                max_sub_length = max(0, min(i+1, chain_length-i)-2)
#                sub_chain = []
#                upNotDown = random.getrandbits(1)
#                for s in range(max_sub_length):
#                    newCarbon = None
#                    if upNotDown:
#                        newCarbon = Carbon(x, y+s+1)
#                    else:
#                        newCarbon = Carbon(x, y-s-1)
#                    sub_chain.append(Carbon)
#                alkane.addSubstituent(Substituent(sub_chain))
#                alkane.carbons.extend(sub_chain)
                

#    def __init__(self, query):  #query will generally be in smiles or inchi
#        self.query = query
#        self.compound_maybe = Compound(get_csid(query))  #uses cactus search to find csid & constructs compound with it
#
#        pass
#
#if __name__ == '__main__':
#    #testing
#    a = Alkane('C')                 #C Methane
#    b = Alkane('CC(C)CC')           #CC(C)CC 2-Methylbutane
#    c = Alkane('CC(C)(C)C')         #CC(C)(C)C 2,2-Dimethylpropane
#
#    print(a.compound_maybe.smiles) #a
#    print(a.compound_maybe.iupac)
#    print(b.compound_maybe.smiles) #b
#    print(b.compound_maybe.iupac)
#    print(c.compound_maybe.smiles) #c
#    print(c.compound_maybe.iupac)
#    pass

