# -*- coding: utf-8 -*-

"""
CactusAPI

Simple Python wrapper for the Cactus API.
Used ChemSpiPy for guidance

"""

import urllib2

__author__ = 'Roland Heintze'
__email__ = 'rheintze@linux.com'
__version__ = '1.0'

def get_csid(query):
    """ searches for a csid based on search query, smiles/inchi preferred """
    searchurl = 'http://cactus.nci.nih.gov/chemical/structure/%s/chemspider_id' % (urllib2.quote(query))
    response = urllib2.urlopen(searchurl).readline()
    return response
def get_iupac(smiles_query):
    """  uses smiles to pull compound's IUPAC from cactus """

    assert type(smiles_query) == str or type(smiles_query) == str, 'query not a string object'
    searchurl = 'http://cactus.nci.nih.gov/chemical/structure/%s/iupac_name' % (smiles_query)
    response = str(urllib2.urlopen(searchurl).readline())

    return response


if __name__ == '__main__':
    print(get_csid('C'))
    print(get_iupac('C'))
    print(get_csid('CC(C)CC'))
    print(get_iupac('CC(C)CC'))
    print(get_csid('CC(C)(C)C'))
    print(get_iupac('CC(C)(C)C'))