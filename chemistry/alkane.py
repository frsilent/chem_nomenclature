__author__ = 'rheintze'

#from chemspipy import *
#from cactusAPI import get_csid
from chemistry.carbon import Carbon
from chemistry.substituent import Substituent
from chemistry.chem_exceptions import *
from random import randint
class Alkane:
    """
    A class used to implement an organic compound.
    """

    CHAIN_NAMES = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane',
             'undecane','dodecane','tridecane','tetradecane','pentadecane')
    MAX_CHAIN_LENGTH = len(CHAIN_NAMES)-1
    
    
    #Raises EmptyAlkaneErorr, CyclicAlkaneError, AlkaneNotConnectedErrorr, LongestChainTooLongError,
    #BranchingCarbonChainError, SubstituentTooLargeError, TooManyOfOneSubstituentGroupError
    def __init__(self, matrix, carbonList = None):
        self.carbons = [] #list of all nodes (carbons) in the graph (molecule)
        self.head = None
        #Initialize head and carbons to represent a graph of carbons
        self.initGraph(matrix, carbonList)
        if self.head == None:
            raise EmptyAlkaneError()
        #Raises CyclicAlkaneError for Alkanes with loops and blocks of carbons
        if not self.isConnected():
            raise AlkaneNotConnectedError()
        #Raises LongestChainTooLongError for molecules too large for us to name
        self.longestChain = self.getLongestChain()
        #Raises BranchingCarbonChainError for malformed substituents
        #Raises SubstituentTooLargeError for substituents that are larger than we can name
        self.setSubstituents()
        self.setCorrectHead()
        #Raises TooManyOfOneSubstituentGroupError if there are too many of a single type of substituent
        Substituent.validateSubs(self.substituents)
        self.name = self.getName()


    #Initialize graph and carbon list based on carbon matrix
    def initGraph(self, graphicMatrix, carbonList):
        #Did we only get passed a list of carbons?
        if not graphicMatrix:
            self.carbons = carbonList
        #We were passed a boolean matrix
        else:
            width = len(graphicMatrix)
            height = len(graphicMatrix[0])
            #Iterate over the matrix and add carbons
            #to our list appropriately
            for col_index in range(0, width):
                for row_index in range(0, height):
                    #Skip empty spaces
                    if not graphicMatrix[col_index][row_index]:
                        continue
                    #If this square is occupied, add a relevant carbon to our list
                    self.carbons.append(Carbon(col_index, row_index))
        #Do we have any carbons?
        if any(self.carbons):
            #Then set the head to the first one (for now, until we find the real head later)
            self.head = self.carbons[0]
        #Form bonds between adjacent Carbons
        Carbon.bondCarbons(self.carbons)
        

    #Check if carbons are connected and graph has no cycles
    #Raises CyclicAlkaneError if this molecule contains any cycles
    def isConnected(self):
        totalSet = set(self.carbons)
        #Raises CyclicAlkane Error if any cycles exist
        connectedSet = self.head.getConnectedSet()
        return totalSet == connectedSet
    
    #Throws LongestChainTooLong for molecules with longest chains that are too long
    def getLongestChain(self):
        #The longest chain per carbon atom
        candidateLongestChains = []
        for carbon in self.carbons:
            candidateLongestChains.append(carbon.getLongestChain())
        #Return the longest chain
        longestChain = max(candidateLongestChains, key=len)
        #Is our longest chain too long for us to name?
        if len(longestChain) > Alkane.MAX_CHAIN_LENGTH:
            #Then raise an error to the caller
            raise LongestChainTooLongError()
        return longestChain

    def setSubstituents(self):
        subs = []
        #Iterate over the longest chain
        for i in range(len(self.longestChain)):
            current = self.longestChain[i]
            validDirs = list(Carbon.directions())
            #Is this not the first carbon?
            if i != 0:
                #Then make sure we don't look backwards in the 
                #chain for substituents
                previousCarbon = self.longestChain[i-1]
                prevDir = current.getDirectionTo(previousCarbon)
                validDirs.remove(prevDir)
            #Is this not the last carbon?
            if i != len(self.longestChain)-1:
                #Then make sure we don't look forwards in the 
                #chain for substituents
                nextCarbon = self.longestChain[i+1]
                nextDir = current.getDirectionTo(nextCarbon)
                validDirs.remove(nextDir)
            #Iterate over all directions that aren't connected to 
            #carbons in the longest chain
            for subDirection in validDirs:
                #Get the carbon in this direction
                subCarbon = getattr(current, subDirection)
                #Is there a carbon for a substituent here?
                if subCarbon:
                    #Add a new substituent to our list of substituents
                    #Raises SubstituentTooLargeError for substituents that are too long
                    #Raises BranchingCarbonChainError for malformed substituents
                    subs.append(Substituent(current, subDirection, i+1))
        #Update our list of substituents
        self.substituents = subs

    def getName(self):
        #The name of the molecule represented by the longest chain
        basename = Alkane.CHAIN_NAMES[len(self.longestChain)-1]
        #The part of the name derived from the substituents
        subname = Substituent.getName(self.substituents)
        return subname+basename

    def verify(self,guess):
        return guess == self.getName()
    
    def getCarbons(self):
        return self.carbons
    
    #Get the correct head. That is, the end of the longest chain that
    # is closest to a substituent
    def setCorrectHead(self):
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
            #Was the tail of self.longesetChain the correct head?
            if winningIndex:
                #Reverse the longest chain
                self.longestChain.reverse()
                #Set the correct head
                self.head = self.longestChain[0]
                #Get substituents again, so that their indices are correct
                self.substituents = self.setSubstituents()
        
    @staticmethod   
    def createRandomAlkane():
        #Pick a random chain length
        chainLength = randint(1,Alkane.MAX_CHAIN_LENGTH)
        carbons = []
        yOffset = 5
        xOffset = 2
        for chainIndex in range(chainLength):
            #Add a longest chain carbon to our list
            carbons.append(Carbon(xOffset+chainIndex, yOffset))
            #Randomly (weighted to fail) add a substituent
            if not randint(0,3):
                #Our max sub length needs to not be part of the longest chain and not overflow our window
                subLength = max(0, min(chainIndex+1, chainLength-chainIndex)-2)%4
                #Add substituents increasing in y if we're at an odd index
                #This prevents adjacent substituents from forming
                upNotDown = chainIndex % 2
                #Iterate over the predetermined length of this new substituent
                for subIndex in range(subLength):
                    nextSubCarbon = None
                    #Should we draw up to avoid drawing next to our neighbors?
                    if upNotDown:
                        nextSubCarbon = Carbon(chainIndex+xOffset, yOffset+subIndex+1)
                    #We should draw down to avoid drawing next to our neighbors.
                    else:
                        nextSubCarbon = Carbon(chainIndex+xOffset, yOffset-subIndex-1)
                    #Add this new carbon to our list of carbons
                    carbons.append(nextSubCarbon)
        return Alkane(None,carbons)
