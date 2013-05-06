# -*- coding: utf-8 -*-

"""
CactusAPI

Simple Python wrapper for the Cactus API.
Used ChemSpiPy for guidance

"""

import urllib.request

__author__ = 'Roland Heintze'
__email__ = 'rheintze@linux.com'
__version__ = '1.0'

def get_csid(query):
    """ searches for a csid based on search query, smiles/inchi preferred """
    searchurl = 'http://cactus.nci.nih.gov/chemical/structure/%s/chemspider_id' % (urllib.parse.quote(query))
    response = str(urllib.request.urlopen(searchurl).readline().strip())[2:-1]

    return response
def get_iupac(smiles_query):
    """  uses smiles to pull compound's IUPAC from cactus """

    assert type(smiles_query) == str or type(smiles_query) == str, 'query not a string object'
    searchurl = 'http://cactus.nci.nih.gov/chemical/structure/%s/iupac_name' % (urllib.parse.quote(smiles_query))
    response = str(urllib.request.urlopen(searchurl).read())[2:-1]

    return response


if __name__ == '__main__':
    print(get_csid('C'))
    print(get_iupac('C'))
    print(get_csid('CC(C)CC'))
    print(get_iupac('CC(C)CC'))
    print(get_csid('CC(C)(C)C'))
    print(get_iupac('CC(C)(C)C'))