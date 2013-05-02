from chemistry.carbon import Carbon
class Substituent():
    
    names = ('methyl','ethyl','propyl','butyl','pentyl')
    MAX_SUB_LENGTH = len(names)       
    
    def __init__(self, carbon, direction, index):
        #Throws BranchingCarbonChainError for malformed substituents
        self.carbons=carbon.getCarbonsInDirection(direction)
        self.index=index

    def getName(self):
        carbon_length = len(self.carbons)
        return "%d-%s" % (self.index, Substituent.names[carbon_length-1])
    
    #Return the first carbon in the sequence, the one adjacent to the longest chain
    def getHead(self):
        return self.carbons[0]