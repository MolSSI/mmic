import sys
import numpy
import os

sys.path.insert(0, '..')

# import models
from models.components.utils.input import FileInput
from models.domains.classmech.molecule import MMolecule
from models.tools.rdkit.codes import ChemCode

# import converter component
from components.implementation.utils.mm_reader import MMoleculeReader, MMoleculeReaderInput

# Test input file
pdbFile = FileInput(path=os.path.abspath('../data/dialanine/dialanine.pdb'))

sdfFile = FileInput(path=os.path.abspath('../data/dummy_ligand/ligand.sdf'))
smiles = ChemCode(code='CCC')

#mmInput = MMoleculeReaderInput(code=smiles)
#mmolec  = MMoleculeReader.compute(mmInput)

mol = MMolecule.from_file(filename=pdbFile.path)

print("MMolecule info:")
print("===============")
print(mol.geometry)
