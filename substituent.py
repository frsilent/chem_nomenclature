from carbon import Carbon
class Substituent():
    
    def __init__(self, carbons, index):
     self.head = carbons[0]
     self.carbons=carbons
     self.index=index

    #Raises BranchingCarbonChainError for malformed substituents                
    @staticmethod
    def getSubsituentsAt(longestChain, index):
        subs = []
        for i in range(len(longestChain)):
            head = longestChain[i]
            #All directions that don't link to longest chain are valid
            #directions for a substituent
            validSubDirections = list(Carbon.directions())
            print(validSubDirections) 
            #Is this not the first one?
            if i>0:
                previousCarbon = longestChain[i-1]
                invalidDirection = head.getDirectionTo(previousCarbon)
                validSubDirections.remove(invalidDirection)
            #Is this not the last one?
            if i+1 < len(longestChain):
                nextCarbon = longestChain[i+1]
                invalidDirection = head.getDirectionTo(nextCarbon)
                validSubDirections.remove(invalidDirection)
            
            for dir in validSubDirections:
                #Is there a carbon chain here?
                subCandidate = getattr(head, dir) 
                if subCandidate:
                    try:
                        carbons = head.getCarbonsInDirection(direction = dir)
                    except BranchingCarbonChainError as error:
                        raise error
                    subs.append(Substituent(carbons = carbons, index = i))
        return subs         