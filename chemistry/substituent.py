from chemistry.carbon import Carbon
class Substituent():
    
    NAMES = ('methyl','ethyl','propyl','butyl','pentyl','hexyl','heptyl','nonyl','decyl')
    PREFIXES = ('', 'di', 'tri', 'tetra', 'penta', 'hexa','hepta','octa','nona','deca')
    MAX_SUB_LENGTH = len(NAMES)       
    
    def __init__(self, carbon, direction, index):
        #Throws BranchingCarbonChainError for malformed substituents
        self.carbons=carbon.getCarbonsInDirection(direction)
        self.index=index

    def getFullName(self):
        carbon_length = len(self.carbons)
        return "%d-%s" % (self.index, Substituent.NAMES[carbon_length-1])
    
    def getAlphaName(self):
        return Substituent.names[len(self.carbons)-1]
    
    #Return the first carbon in the sequence, the one adjacent to the longest chain
    def getHead(self):
        return self.carbons[0]
    
    @staticmethod
    def getName(subs):
        #A mapping of names to a list of indices at which those names occur
        indexDict = {(n, []) for n in Substituent.NAMES}
        for sub in subs:
            #Get the name of the substituent based on length alone
            name = sub.getAlphaName()
            #Add this substituent's index to the list of substituents with the same name
            indexDict[name].append(sub.index)
        
        #Get a copy of the key, value pairs in a list of key, value tuples 
        resultList = indexDict.items()[:]
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
        return subTypeStrs.join('-')
        
    @staticmethod
    def getNameOfSubType(subName, indeces):
        #Did this type of substituent surface in the Alkane?
        if any(indeces):
            #Make sure indices show up in numerical order
            indeces.sort()
            #Cast our indices to strings so we can join them together
            strIndeces = map(str, indeces)
            #Join the indices together with a comma
            indexStr = strIndeces.join(",")
            #Get the relevant prefix based on how many times this 
            #type of substituent was found. That is, the 
            #number of indices, or the length of indices
            prefix = Substituent.PREFIXES[len(indeces)]
            #return a string formatted such as '2,4-dimethyl'
            return indexStr+'-'+prefix+subName
        #This type of substituent was not present in the molecule
        else:
            #So return an empty string so the name isn't
            #added to the name of the molecule
            return ""
        
        
        
        
        