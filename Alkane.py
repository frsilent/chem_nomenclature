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
        compound_maybe = Compound(get_csid(query))  #uses cactus search to find csid & constructs compound with it
        print(compound_maybe.smiles)
        print(compound_maybe.iupac)

        pass

if __name__ == '__main__':
    #testing
    a = Alkane('C')                 #Methane // TODO: FIX THIS. ChemSpider Search is bad.
    b = Alkane('CC(C)CC')           #CC(C)CC 2-Methylbutane
    c = Alkane('CC(C)(C)C')         #CC(C)(C)C 2,2-Dimethylpropane
    pass