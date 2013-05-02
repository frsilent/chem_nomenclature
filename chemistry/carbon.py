from chemistry.chem_exceptions import *

class Carbon:
    """
    A class used to represent a carbon in an alkane molecule
    """

    #Ordered such that directions[i] opposes directions[3-i]
    @staticmethod
    def directions():
        return ('north', 'east', 'west', 'south')
    
    @staticmethod
    def getDirectionsWithout(ignoreDirection):
        dirs = ['north', 'east', 'west', 'south']
        if ignoreDirection:
            dirs.remove(ignoreDirection)
        return tuple(dirs)
    
    @staticmethod
    def getOpposingDirection(direction):
        return Carbon.directions()[3-Carbon.directions().index(direction)]
        
    @staticmethod
    def bondCarbons(carbons):
        for i in range(len(carbons)):
            for j in range(i+1, len(carbons)):
                try:
                    carbons[i].bondTo(carbons[j])
                except:
                    pass
    
    @staticmethod
    def dissolveCarbons(carbons):
        for c in carbons:
            for direction in Carbon.directions():
                setattr(c, direction, None)
    
    def __init__(self, x, y):
        self.north = self.south = self.east = self.west = None
        self.x = x 
        self.y = y 


    def __str__(self):
        result = super().__str__()
        result += "\nX: %d Y: %d\n" % (self.x, self.y)
        for direction in Carbon.directions():
            result += " "+direction+": %s\n" % ("yes " if getattr(self, direction, None) else "no ")
        return result
    
    #Returns longest chain of carbons that includes this carbon,
    #with this carbon as the first one in the list    
    def getLongestChain(self):
        return self._getLongestChain()
    
    #Recursive helper method
    def _getLongestChain(self, ignoreDirection=None):
        #Append this carbon to the chain
        chain = [self]
        #List of carbon chains that are valid candidates for longest chain
        validChains = []
        for direction in Carbon.getDirectionsWithout(ignoreDirection):
            nextCarbon = getattr(self, direction)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(direction)
                validChains.append(nextCarbon._getLongestChain(opposingDirection))
        if any(validChains):
            #Extend our chain with the longest chain we found
            chain.extend(max(validChains, key=len))
        return chain
    
    def getConnectedSet(self):
        return self._getConnectedSet(carbonSet = None)
    
    #Helper recursive method for isConnectedHasCycles
    #TODO: Fix this method to clear the set if carbon is deleted
    def _getConnectedSet(self, carbonSet, ignoreDirection=None):
        if not carbonSet:
            carbonSet = set()
        if self in carbonSet:
            raise CyclicAlkaneError()
        else:
            carbonSet.add(self)
        for direction in Carbon.getDirectionsWithout(ignoreDirection):
            nextCarbon = getattr(self, direction, None)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(direction)
                nextCarbon._getConnectedSet(carbonSet, opposingDirection)
        return carbonSet

    def getNumberOfBonds(self):
        num = 0
        for direction in Carbon.directions():
            if getattr(self,direction, None):
                num+=1
        return num

    def getDirectionTo(self, carbon):
        for direction in Carbon.directions():
            if getattr(self, direction, None) == carbon:
                return direction
        return None
    
    
    def bondTo(self, other):
        #Are these carbons the same or in the same position?
        if self == other or self.x == other.x and self.y == other.y:
            raise CarbonsNotAdjacentError
        #Are we not on the same column and not on the same row?
        if self.x != other.x and self.y != other.y:
            raise CarbonsNotAdjacentError
        else:
            #Are we on the same row?
            if self.y == other.y:
                #Are we one space apart?
                if abs(self.x - other.x) == 1:
                    #Am I on the left?
                    if self.x < other.x:
                        #Bond the carbons together appropriately
                        self.east = other
                        other.west = self
                    #I am on the right
                    else:
                        #Bond the carbons together appropriately
                        self.west = other
                        other.east = self
                #We are too far apart        
                else:
                    raise CarbonsNotAdjacentError
            #We are on the same column
            else:
                #Are we one space apart?
                if abs(self.y - other.y) == 1:
                    #Am I on top?
                    if self.y < other.y:
                        #Bond the carbons together appropriately
                        self.south = other
                        other.north = self
                    #I am on the bottom
                    else:
                        #Bond the carbons together appropriately
                        self.north = other
                        other.south = self
                #We are too far apart
                else:
                    raise CarbonsNotAdjacentError
    
    #Returns a list of carbons from self outward in direction, not including self
    #Throws AmbiguousBranchingPath if any Carbon in the sequence has
    #more than two connected Carbons        
    def getCarbonsInDirection(self, direction):
        result = None
        try:
            result = self._getCarbonsInDirection(direction)
        #Was there a branching, ambiguous path?
        except BranchingCarbonChainError as error:
            #Pass the error along to the caller
            raise error
        #Return the result from the helper method without the first element,
        #which will always equal this
        return result[1:]
    
    #Recursive helper method that returns chain in direction, plus original carbon
    def _getCarbonsInDirection(self, direction, ignoreDirection=None):
        chain = [self]
        #Was this the top-level call? 
        if direction:
            nextCarbon = getattr(self, direction, None)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(direction)
                #search for more carbons and add them to our chain
                chain.extend(nextCarbon._getCarbonsInDirection(None, ignoreDirection=opposingDirection))
            return chain
        else:
            numBonds = self.getNumberOfBonds()
            #Is our only bond the one we came here on, hence a dead end?
            if numBonds == 1:
                return chain
            #Do we have an extra bond to find more carbons on?
            elif numBonds == 2:
                for direction in Carbon.getDirectionsWithout(ignoreDirection):
                    nextCarbon = getattr(self, direction, None) 
                    if nextCarbon:
                        opposingDirection = Carbon.getOpposingDirection(direction)
                        chain.extend(nextCarbon._getCarbonsInDirection(None, opposingDirection))
            #We have too many branches
            else:
                #So throw an exception
                raise BranchingCarbonChainError()
        return chain
    

    def getDistanceTo(self, target, ignoreDirection=None):
        count = 1
        if self == target:
            return 0
        else:
            #List of distance results from recursive calls
            distances = []
            for direction in Carbon.getDirectionsWithout(ignoreDirection):
                nextCarbon = getattr(self, direction)
                if nextCarbon:
                    opposingDirection = Carbon.getOpposingDirection(direction)
                    distance = nextCarbon.getDistanceTo(target, opposingDirection)
                    if distance > -1:
                        distances.append(distance)
            #Did we find our target?
            if len(distances):
                #Add the shortest distance to the target to our count
                count += min(distances)
            #We didn't find our target
            else:
                #So return -1
                count = -1
        return count
            
        
        
        
        
        
        
        
        
        
        
        
        