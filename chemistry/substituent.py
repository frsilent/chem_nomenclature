from chemistry.carbon import Carbon
from chemistry.chem_exceptions import SubstituentTooLargeError, TooManyOfOneSubstituentGroupError
class Substituent():
    
    NAMES = ('methyl','ethyl','propyl','butyl','pentyl','hexyl','heptyl','nonyl','decyl')
    PREFIXES = ('', 'di', 'tri', 'tetra', 'penta', 'hexa','hepta','octa','nona','deca')
    MAX_LENGTH = len(NAMES)
    MAX_FREQUENCY = len(PREFIXES)
    
    #Raises SubstituentTooLargeError for substituents that are larger than we can name
    #Raises BranchingCarbonChainError for malformed substituents
    def __init__(self, carbon, direction, index):
        #Raises BranchingCarbonChainError for malformed substituents
        self.carbons=carbon.getCarbonsInDirection(direction)
        #Is this substituent too large?
        if len(self.carbons) > Substituent.MAX_LENGTH:
            #Then raise an error
            raise SubstituentTooLargeError()
        self.index=index
        
    #Return the name of this substituent without accounting
    #for its position or its neighbors
    def getAlphaName(self):
        return Substituent.NAMES[len(self.carbons)-1]
    
    #Return the first carbon in the sequence, the one adjacent to the longest chain
    def getHead(self):
        return self.carbons[0]
    
    @staticmethod
    def getName(substituentSequence):
        #Were we passed a sequence of substituents to name?
        if substituentSequence:
            #A mapping of names to a list of indices at which those names occur
            indexDict = dict((n, []) for n in Substituent.NAMES)
            for sub in substituentSequence:
                #Get the name of the substituent based on length alone
                name = sub.getAlphaName()
                #Add this substituent's index to the list of substituents with the same name
                indexDict[name].append(sub.index)
            
            #Get a copy of the key, value pairs in a list of key, value tuples 
            resultList = [(name, indeces) for name, indeces in indexDict.items()]
            #Sort the list based on the alphabetical order of the substituent type
            resultList.sort()
            #A list of substituent type strings
            subTypeStrs = []
            for subName, indeces in resultList:
                #Get the name of the group of similar substituents
                subType = Substituent.getNameOfSubType(subName, indeces)
                #Did we get a name for this type of substituent?
                #We would not if it was not in the molecule due to no
                #indices being passed to the function
                if subType:
                    #Then append the name of this substituent type to our list of names
                    subTypeStrs.append(subType)
            #Return the list of substituent type names, joined by hyphens
            return '-'.join(subTypeStrs)
        #We weren't passed any substituents
        else:
            #Return empty string so the caller can count on concatenating with our result
            return ""
        
    @staticmethod
    def getNameOfSubType(subName, indeces):
        #Did this type of substituent surface in the Alkane?
        if any(indeces):
            #Make sure indices show up in numerical order
            indeces.sort()
            #Cast our indices to strings so we can join them together
            strIndeces = map(str, indeces)
            #Join the indices together with a comma
            indexStr = ','.join(strIndeces)
            #Get the relevant prefix based on how many times this 
            #type of substituent was found. That is, the 
            #number of indices, or the length of indices
            prefix = Substituent.PREFIXES[len(indeces)-1]
            #return a string formatted such as '2,4-dimethyl'
            return indexStr+'-'+prefix+subName
        #This type of substituent was not present in the molecule
        else:
            #So return an empty string so the name isn't
            #added to the name of the molecule
            return ""
    
    #Throws TooManyOfOneSubstituentGroupError if there are too many of a single type of substituent
    @staticmethod
    def validateSubs(substituentSequence):
        #Were we passed subsituents to validate?
        if substituentSequence:
            #A mapping of names to the frequency with which they occur in a molecule
            namesToFrequency = dict((n, 0) for n in Substituent.NAMES)
            for sub in substituentSequence:
                #Get the name of the substituent based on length alone
                name = sub.getAlphaName()
                #Increment the count of the substituents with the same name
                namesToFrequency[name]+=1
            #Search our frequencies to look for a substituent that's frequent
            for frequency in namesToFrequency.values():
                #Are there too many of a type of substituent?
                if frequency > Substituent.MAX_FREQUENCY:
                    #Then raise an error to the caller
                    raise TooManyOfOneSubstituentGroupError()
        






