import sys
import numpy
import os

sys.path.insert(0, os.getcwd())
debug = False

# import models
from models.components.utils.input import FileInput
from models.molecmech.molecules.mm_molecule import MMolecule
from models.molecmech.chem.codes import ChemCode

# import converter component
from components.implementation.molecmech.mm_reader import MMoleculeReader, MMoleculeReaderInput

# Test input file
pdbFile = FileInput(path=os.path.abspath('data/dialanine/dialanine.pdb'))

sdfFile = FileInput(path=os.path.abspath('data/dummy_ligand/ligand.sdf'))
smiles = ChemCode(code='CCC')

#mmInput = MMoleculeReaderInput(code=smiles)
#mmolec  = MMoleculeReader.compute(mmInput)

mol = MMolecule.from_file(filename=pdbFile.path)

if debug:
	print("MMolecule info:")
	print("===============")

	print("Bonds:")
	print("======")
	print(mol.connectivity)

	print("Residues:")
	print("==========")
	print(mol.residues)

	print("Positions:")
	print("==========")
	print(mol.geometry)

	print("Atom Names:")
	print("==========")
	print(mol.atom_labels)


mol.to_file('tmp.pdb')
