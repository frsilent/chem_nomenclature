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
    MAX_CHAIN_LENGTH = len(chain)
#    def __init__(self, longestChain):
#        self.carbons = longestChain[:]
#        self.longestChain = longestChain
#        self.head = longestChain[0]

    #Raises EmptyAlkaneErorr, CyclicAlkaneError, AlkaneNotConnectedErrorr, BranchingCarbonChainError
    def __init__(self, matrix):
        self.carbons = [] #list of all nodes (carbons) in the graph (molecule)
        self.head = None
        self.initGraph(matrix)
        if self.head == None:
            raise EmptyAlkaneError()
        #Raises CyclicAlkaneError
        if not self.isConnected():
            raise AlkaneNotConnectedError()
        self.longestChain = self.getLongestChain()
        #Throws BranchingCarbonChainError for malformed substituents
        self.substituents = self.getSubstituents()
        self.head = self.getCorrectHead()
#        self.name = self.getName()
#            raise error


    #Initialize graph and carbon list based on carbon matrix
    def initGraph(self, graphicMatrix):
        width = len(graphicMatrix)
        height = len(graphicMatrix[0])
        for col_index in range(0, width):
            for row_index in range(0, height):
                #Skip empty spaces
                if not graphicMatrix[col_index][row_index]:
                    continue
                thisCarbon = Carbon(col_index, row_index)
                self.carbons.append(thisCarbon)
        if any(self.carbons):
            self.head = self.carbons[0]
        Carbon.bondCarbons(self.carbons)
        

    #Check if carbons are connected and graph has no cycles
    #Raises CyclicAlkaneError if this molecule contains any cycles
    def isConnected(self):
        totalSet = set(self.carbons)
        #Raises CyclicAlkane Error if any cycles exist
        connectedSet = self.head.getConnectedSet()
        return totalSet == connectedSet
    
    def getLongestChain(self):
        #The longest chain per carbon atom
        candidateLongestChains = []
        for carbon in self.carbons:
            candidateLongestChains.append(carbon.getLongestChain())
        #Return the longest chain
        return max(candidateLongestChains, key=len)

    def getSubstituents(self):
        subs = []
        for i in range(len(self.longestChain)):
            current = self.longestChain[i]
            validDirs = list(Carbon.directions())
            if i != 0:
                previousCarbon = self.longestChain[i-1]
                prevDir = current.getDirectionTo(previousCarbon)
                validDirs.remove(prevDir)
            if i != len(self.longestChain)-1:
                nextCarbon = self.longestChain[i+1]
                nextDir = current.getDirectionTo(nextCarbon)
                validDirs.remove(nextDir)
                
            for subDirection in validDirs:
                subCarbon = getattr(current, subDirection)
                if subCarbon:
                    #Throws BranchingCarbonChainError for malformed substituents
                    subs.append(Substituent(current, subDirection, i))
        return subs

    def getName(self):
        basename = self.chain[len(self.getLongestChain())-1]

    def verify(self,guess):
        return guess == self.getName()
    
    def getCarbons(self):
        return self.carbons
    
    #Get the correct head. That is, the end of the longest chain that
    # is closest to a substituent
    def getCorrectHead(self):
        #Mapping of candidates for head (the ends of the longest chain) to distance of closest substituent
        candidates = [
            self.longestChain[0],
            self.longestChain[-1],
        ]
        closestDistances = [None, None]
        for sub in self.substituents:
            for i in range(len(candidates)):
                subDist = candidates[i].getDistanceTo(sub.getHead())
                #Did we find this substituent's head?
                # and is this distance smaller than what we have so far?
                if subDist != -1 and (closestDistances[i] == None or subDist < closestDistances[i]):
                    #Then set the closest distance for this candidate to this distance
                    closestDistances[i] = subDist
        #Did the second candidate not find any substituents?
        if closestDistances[1] == None:
            return candidates[0]
        #Did the first candidate not find any substituents?
        elif closestDistances[0] == None:
            return candidates[1]
        #Both candidates found substituents
        else:
            #Get the index of the candidate with the closest substituent
            winningIndex = closestDistances.index(min(closestDistances))
            print(str(winningIndex))
            return candidates[winningIndex]
        
        
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
