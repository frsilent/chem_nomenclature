class Carbon:
    """
    A class used to represent a carbon in an alkane molecule
    """
    #Ordered such that directions[i] opposes directions[3-i]
    directions = ('north', 'east', 'west', 'south')
    
    def __init__(self):
        self.north = self.south = self.east = self.west = None
    
    def getLongestChain(self):
        return self._getLongestChain()            
    
    def _getLongestChain(self, carbon=self, ignoreDirection=None):
        #Append this carbon to the chain
        chain = [carbon]
        #List of directions that have carbons and are not ignoreDirection
        validDirections = []
        for dir in Carbon.directions:
            if dir == ignoreDirection:
                continue
            if getattr(carbon, dir):
                validDirections.append(dir)
        #Are there branches we need to add to our chain? 
        if any(validDirections):
            validChains = []
            #Populate validChains with lists of Carbons
            for dir in validDirections:
                opposingDirection = Carbon.directions[3-Carbon.directions.index(dir)]
                validChains.append(getLongestChain(carbon = getattr(carbon, dir), ignoreDirection = opposingDirection))
            #Extend our chain with the longest chain we found
            chain.extend(max(validChains, key=len))
        return chain
    
    def getConnectedSet(self):
        return self._getConnectedCarbonSet()
    
    #Helper recursive method for isConnectedHasCycles    
    def _getConnectedSet(self, carbon=self, carbonSet=set(), ignoreDirection=None):
        #Ordered such that directions[i] opposes directions[3-i] 
        directions = ('north', 'east', 'west', 'south')
        if carbon in carbonSet:
            raise CyclicAlkeneError()
        else:
            carbonSet.append(carbon)
        for dir_index in range(len(directions)):
            if ignoreDirection and directions[dir_index] == ignoreDirection:
                continue
            nextCarbon = getattr(carbon, direction)
            if nextCarbon:
                self._getConnectedCarbonSet(nextCarbon, carbonSet, directions[3-dir_index])
        return carbonSet
    
    def getNumberOfBonds(self):
        num = 0
        for dir in Carbon.directions:
            if getattr(self,dir):
                num+=1
        return num
