# -*- coding: utf-8 -*-

"""
CactusAPI

Simple Python wrapper for the Cactus API.
Used ChemSpiPy for inspiration/guidance

"""

import urllib.request, urllib.error, urllib.parse

__author__ = 'Roland Heintze'
__email__ = 'rheintze@linux.com'
__version__ = '1.0'


class Compound(object):
    """ A class for retrieving record details about a compound

    This class provides access to various parts of the Cactus API.
    Further information can be found at http://cactus.nci.nih.gov/chemical/structure
    """

    def __init__(self,query):
        if type(query) is str:
            self.query = query
        else:
            raise TypeError('Query must be a string')

def get_iupac(smiles_query):

    assert type(smiles_query) == str or type(smiles_query) == str, 'query not a string object'
    searchurl = 'http://cactus.nci.nih.gov/chemical/structure/%s/iupac_name' % (urllib.parse.quote(smiles_query))
    response = str(urllib.request.urlopen(searchurl).read())[2:-1]

    return response