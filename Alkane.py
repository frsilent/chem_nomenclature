__author__ = 'rheintze'

from chemspipy import *

class Alkane:
    """
    A class used to implement an organic compound.
    """

    chain = ('methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane',
             'undecane','dodecane','tridecane','tetradecane','pentadecane')
    substituent = ('methyl','ethyl','propyl','butyl','pentyl')

    def __init__(self, smiles):
        #simplified molecular-input line-entry system, an ascii representation of a molecular graph
        self.smiles = smiles

        #Thinking of getting rid of chemspider API & switching to Cactus exclusively
        #Alternatively using Cactus' http://cactus.nci.nih.gov/chemical/structure/C/chemspider_id format
        #Then generating compound with it
        compound_maybe = find_one(smiles)
        print(compound_maybe.smiles)
        print(compound_maybe.iupac)

        pass

if __name__ == '__main__':
    #testing
    a = Alkane('C')                 #Methane // TODO: FIX THIS. ChemSpider Search is bad.
    b = Alkane('CC(C)CC')           #CC(C)CC 2-Methylbutane
    c = Alkane('CC(C)(C)C')         #CC(C)(C)C 2,2-Dimethylpropane
    pass