import sys
import numpy
import os

sys.path.insert(0, os.getcwd())
debug = False

# import models
from mmcomponents.models.components.utils.input import FileInput
from mmelemental.models.molecmech.molecules.mm_molecule import Molecule
from mmelemental.models.molecmech.chem.codes import ChemCode

# import converter component
from components.implementation.molecmech.mm_reader import MoleculeReader, MoleculeReaderInput

# Test input file
pdbFile = FileInput(path=os.path.abspath('data/dialanine/dialanine.pdb'))

sdfFile = FileInput(path=os.path.abspath('data/dummy_ligand/ligand.sdf'))
smiles = ChemCode(code='CCC')

#mmInput = MoleculeReaderInput(code=smiles)
#mmolec  = MoleculeReader.compute(mmInput)

mol = Molecule.from_file(filename=pdbFile.path)

if debug:
	print("Molecule info:")
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
