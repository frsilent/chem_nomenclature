from custom_exceptions import *

class Carbon:
    """
    A class used to represent a carbon in an alkane molecule
    """

    #Ordered such that directions[i] opposes directions[3-i]
    @staticmethod
    def directions():
        return ('north', 'east', 'west', 'south')
    @staticmethod
    def getOpposingDirection(direction):
        return Carbon.directions()[3-Carbon.directions().index(direction)]
        
    def __init__(self):
        self.north = self.south = self.east = self.west = None
        self.visited = False #access flag; used for longestChain

    def getLongestChain(self):
        return self._getLongestChain()
    
    def _getLongestChain(self, ignoreDirection=None):
        #Append this carbon to the chain
        chain = [self]
        #List of directions that have carbons and are not ignoreDirection
        validChains = []
        for dir in Carbon.directions():
            if dir == ignoreDirection:
                continue
            if getattr(self, dir):
                opposingDirection = Carbon.getOpposingDirection(dir)
                nextCarbon = getattr(self, dir)
                validChains.append(nextCarbon._getLongestChain(opposingDirection))
            if any(validChains):
                #Extend our chain with the longest chain we found
                chain.extend(max(validChains, key=len))
        return chain
    
    def getConnectedSet(self):
        return self._getConnectedCarbonSet()
    
    #Helper recursive method for isConnectedHasCycles
    #TODO: Fix this method to clear the set if carbon is deleted
    def getConnectedSet(self, carbonSet=set(), ignoreDirection=None):
        #Ordered such that directions[i] opposes directions[3-i]
        directions = ('north', 'east', 'west', 'south')
        if self in carbonSet:
            raise CyclicAlkaneError()
        else:
            carbonSet.add(self)
        for dir in directions:
            if dir == ignoreDirection:
                continue
            nextCarbon = getattr(self, dir)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(dir)
                nextCarbon.getConnectedSet(carbonSet, opposingDirection)
        return carbonSet

    def getNumberOfBonds(self):
        num = 0
        for dir in Carbon.directions():
            if getattr(self,dir):
                num+=1
        return num

    def getDirectionTo(self, carbon):
        for direction in Carbon.directions():
            if getattr(self, direction) == carbon:
                return direction
        return None
    
    #Throws AmbiguousBranchingPath if any Carbon in the sequence has
    #more than two connected Carbons
    def getCarbonsInDirection(self, direction, ignoreDirection=None):
        chain = [self]
        if direction:
            nextCarbon = getattr(self, direction)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(direction)
                chain.extend(nextCarbon.getCarbonsInDirection(direction=None, ignoreDirection=opposingDirection))
        else:
            #To check for branching paths 
            hasChain = False
            for dir in Carbon.directions():
                if dir == ignoreDirection:
                    continue
                nextCarbon = getattr(self, dir) 
                if nextCarbon:
                    #If we find a second chain, raise an error. The chain would be ambiguous.
                    if hasChain:
                        raise BranchingCarbonChainError()
                    opposingDirection = Carbon.getOpposingDirection(direction)
                    #Search for more Carbons and add them to our list
                    chain.extend(nextCarbon.getCarbonsInDirection(direction=None, ignoreDirection=opposingDirection))
                    hasChain=True
        return chain
            