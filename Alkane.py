__author__ = 'rheintze'


class Alkane:
    """
    A class used to implement an organic compound.
    """

    chain = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane')
    substituent = ('methyl','ethyl','propyl','butyl','pentyl')
    def init(self, longestChain, noSub):
        #integers longestChain, maxSubLength, & subPosition[]
        self.longestChain = longestChain
        pass

if __name__ == '__main__':
    #testing
    a = Alkane()
    pass