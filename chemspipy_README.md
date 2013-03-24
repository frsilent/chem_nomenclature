# ChemSpiPy

Python wrapper for the ChemSpider API.

Forked from [ChemSpiPy by Cameron Neylon](https://github.com/cameronneylon/ChemSpiPy).

## Usage

    import chemspipy
    
    # Specify compound by ChemSpider ID
    c = Compound('236')
    
    # Search using name, SMILES, InChI, InChIKey, etc.
    c = chemspipy.find_one('benzene')
    c = chemspipy.find('benzene')[0]

Properties of the compound class:

	c.imageurl
	c.mf
	c.smiles
	c.inchi
	c.inchikey
	c.averagemass
	c.molecularweight
	c.monoisotopicmass
	c.nominalmass
	c.alogp
	c.xlogp
	c.commonname
	c.image
	c.mol
