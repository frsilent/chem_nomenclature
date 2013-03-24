__author__ = 'rheintze'

from chemspipy import *

class Alkane:
    """
    A class used to implement an organic compound.
    """

    chain = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane')
    substituent = ('methyl','ethyl','propyl','butyl','pentyl')

    def __init__(self, smiles):
        self.smiles = smiles #simplified molecular-input line-entry system, an ascii representation of a molecular graph
        print(smiles)
        #modify smiles to match correct query
        compound_maybe = find_one(smiles)
        print(compound_maybe.commonname)
        print(compound_maybe.smiles)
        print(compound_maybe.mol)

        #once a compound is identified it can be pulled from chemspider
        #then initialized as a compound using Compound(id)
        #x = Compound(236)
        #print(x.imageurl)

        pass

if __name__ == '__main__':
    #testing
    a = Alkane('CC(C)CC')           #CC(C)CC 2-Methylbutane
    #b = Alkane('CC(C)(C)C')         #CC(C)(C)C 2,2-Dimethylpropane
    pass