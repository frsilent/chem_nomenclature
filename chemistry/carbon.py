from chemistry.chem_exceptions import *

class Carbon:
    """
    A class used to represent a carbon in an alkane molecule
    """
    
    #Return a new tuple of strings that represent the carbon pointer attributes of all carbon instances
    @staticmethod
    def directions():
        #Ordered such that directions[i] opposes directions[3-i]
        return ('north', 'east', 'west', 'south')
    
    #Used frequently by functions that iterate over carbons
    @staticmethod
    def getDirectionsWithout(ignoreDirection):
        dirs = ['north', 'east', 'west', 'south']
        if ignoreDirection:
            dirs.remove(ignoreDirection)
        return tuple(dirs)
    
    #Utility method for getting the opposite direction
    @staticmethod
    def getOpposingDirection(direction):
        return Carbon.directions()[3-Carbon.directions().index(direction)]
   
    #Bond adjacent carbons together and ignore carbons that aren't close enough to bond
    @staticmethod
    def bondCarbons(carbons):
        for i in range(len(carbons)):
            for j in range(i+1, len(carbons)):
                try:
                    carbons[i].bondTo(carbons[j])
                except:
                    pass
    
    #Remove all bonds between all carbons in the sequence
    @staticmethod
    def dissolveCarbons(carbons):
        for c in carbons:
            for direction in Carbon.directions():
                setattr(c, direction, None)
    
    #Constructor
    def __init__(self, x, y):
        self.north = self.south = self.east = self.west = None
        self.x = x 
        self.y = y 

    #Enables use of str(myCarbon)
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
        #Initialize our results list with self
        chain = [self]
        #List of carbon chains that are valid candidates for longest chain
        validChains = []
        for direction in Carbon.getDirectionsWithout(ignoreDirection):
            nextCarbon = getattr(self, direction)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(direction)
                validChains.append(nextCarbon._getLongestChain(opposingDirection))
        #Did we find any other carbons?
        if any(validChains):
            #Extend our chain with the longest chain we found
            chain.extend(max(validChains, key=len))
        return chain
    
    #Traverses this carbon's network to return all carbons connected to this one
    def getConnectedSet(self):
        return self._getConnectedSet(carbonSet = None)
    
    #Helper recursive method for getConnectedSet
    def _getConnectedSet(self, carbonSet, ignoreDirection=None):
        #Were we not passed a set of carbons?
        if not carbonSet:
            #Then set up a new set of carbons
            carbonSet = set()
        #Are we already in the set we were passed?
        if self in carbonSet:
            #Then raise an error for the caller
            raise CyclicAlkaneError()
        #We were not already in the set
        else:
            #So add ourself to the set
            carbonSet.add(self)
        #Iterate over directions we haven't been to yet
        for direction in Carbon.getDirectionsWithout(ignoreDirection):
            #The next carbon in this direction
            nextCarbon = getattr(self, direction, None)
            #Do we have a carbon in this direction?
            if nextCarbon:
                #Then search that carbon and its neighbors for duplicates
                opposingDirection = Carbon.getOpposingDirection(direction)
                nextCarbon._getConnectedSet(carbonSet, opposingDirection)
        #Return our set of carbons, those that we are connected to
        return carbonSet

    #Count the number of bonds that aren't None
    def getNumberOfBonds(self):
        num = 0
        #Iterate over all of our own valid directions
        for direction in Carbon.directions():
            if getattr(self,direction, None):
                num+=1
        return num

    #If this carbon is directly connected to carbon,
    #return the direction from self to carbon
    def getDirectionTo(self, carbon):
        #Iterate over our carbons  directly connected to ourself
        for direction in Carbon.directions():
            #Did we find the carbon we were looking for?
            if getattr(self, direction, None) == carbon:
                #Then return the direction we found it in
                return direction
        #If we didn't find the carbon, return None
        return None
    
    #Bond two carbons together correctly based on logical coordinates
    #If they are too far apart, raise an exception
    def bondTo(self, other):
        #Are these carbons the same or in the same position?
        if self == other or self.x == other.x and self.y == other.y:
            #Then raise an error
            raise CarbonsNotAdjacentError
        #Are we not on the same column and not on the same row?
        if self.x != other.x and self.y != other.y:
            #Then raise an error
            raise CarbonsNotAdjacentError
        #We are on the same row or the same column
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
                    #So raise an error
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
                    #So raise an error
                    raise CarbonsNotAdjacentError
    
    #Returns a list of carbons from self outward in direction, not including self
    #Throws AmbiguousBranchingPath if any Carbon in the sequence has
    #more than two connected Carbons        
    def getCarbonsInDirection(self, direction):
        #Return the result from the helper method without the first element,
        #which will always equal this
        #Raises BranchingCarbonChainError if the chain from self in this direction branches
        return self._getCarbonsInDirection(direction)[1:]
    
    #Recursive helper method that returns chain in direction, plus original carbon
    def _getCarbonsInDirection(self, direction, ignoreDirection=None):
        #Initialize our results with ourself
        chain = [self]
        #Was this the top-level call? 
        if direction:
            nextCarbon = getattr(self, direction, None)
            if nextCarbon:
                opposingDirection = Carbon.getOpposingDirection(direction)
                #search for more carbons and add them to our chain
                chain.extend(nextCarbon._getCarbonsInDirection(None, ignoreDirection=opposingDirection))
            return chain
        #This was not the top-level call
        else:
            #Use the number of bonds to determine what to do
            numBonds = self.getNumberOfBonds()
            #Is our only bond the one we came here on, hence a dead end?
            if numBonds == 1:
                return chain
            #Do we have a single, unambiguous extra bond to find more carbons on?
            elif numBonds == 2:
                #Search for that extra, unvisited bond
                for direction in Carbon.getDirectionsWithout(ignoreDirection):
                    #Get the next carbon in this direction
                    nextCarbon = getattr(self, direction, None)
                    #Do we have a carbon in this direction?
                    if nextCarbon:
                        #Add the carbons in this line to our result
                        opposingDirection = Carbon.getOpposingDirection(direction)
                        chain.extend(nextCarbon._getCarbonsInDirection(None, opposingDirection))
            #We have too many branches
            else:
                #So throw an exception
                raise BranchingCarbonChainError()
        #Return our results to the caller
        return chain
    
    #Recursively get the distance from this carbon to target
    #as an integer, computed by following carbon bonds.
    #Return -1 if we don't find it.
    def getDistanceTo(self, target, ignoreDirection=None):
        #Are we looking for ourself?
        if self == target:
            #Then return 0
            return 0
        else:
            #List of distance results from recursive calls
            distances = []
            #Iterate over unvisited directions
            for direction in Carbon.getDirectionsWithout(ignoreDirection):
                #Get the carbon in this direction
                nextCarbon = getattr(self, direction)
                #Does that carbon exist?
                if nextCarbon:
                    #Get the distance from ourself to target via this carbon
                    opposingDirection = Carbon.getOpposingDirection(direction)
                    distance = nextCarbon.getDistanceTo(target, opposingDirection)
                    #Did we find our target this time?
                    if distance > -1:
                        #Then add the distance to our list of distances
                        distances.append(distance)
            #Initialize count to one to represent looking at this carbon
            count = 1
            #Did we find our target at least once?
            if len(distances):
                #Add the shortest distance to the target to our count
                count += min(distances)
            #We didn't find our target
            else:
                #So return -1
                count = -1
        #Return our result to the caller
        return count