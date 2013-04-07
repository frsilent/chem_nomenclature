__author__ = 'rheintze'

from chemspipy import *
from cactusAPI import get_csid

class Alkane:
    """
    A class used to implement an organic compound.
    """

    chain = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane',
             'undecane','dodecane','tridecane','tetradecane','pentadecane')
    substituent = ('methyl','ethyl','propyl','butyl','pentyl')

    def __init__(self, query):  #query will generally be in smiles or inchi
        self.query = query
        self.compound_maybe = Compound(get_csid(query))  #uses cactus search to find csid & constructs compound with it

        pass

if __name__ == '__main__':
    #testing
    a = Alkane('C')                 #C Methane
    b = Alkane('CC(C)CC')           #CC(C)CC 2-Methylbutane
    c = Alkane('CC(C)(C)C')         #CC(C)(C)C 2,2-Dimethylpropane

    print(a.compound_maybe.smiles) #a
    print(a.compound_maybe.iupac)
    print(b.compound_maybe.smiles) #b
    print(b.compound_maybe.iupac)
    print(c.compound_maybe.smiles) #c
    print(c.compound_maybe.iupac)
    pass