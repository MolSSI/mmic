import sys
import numpy
import os

sys.path.insert(0, os.getcwd())

# import models
from models.components.utils.input import FileInput
from models.components.docking.input import DockingPrepInput
from models.molecmech.chem.codes import ChemCode

# import converter component
from components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent

# Test input file
pdbFile = FileInput(path=os.path.abspath('data/dialanine/dialanine.pdb'))

print('pdbFile.ext = ', pdbFile.ext)

sdfFile = FileInput(path=os.path.abspath('data/dummy_ligand/ligand.sdf'))
smiles = ChemCode(code='CCC')

dockPrepInput = DockingPrepInput(ligand=smiles, receptor=pdbFile)

dockInput = ConvertAutoDockComponent.compute(dockPrepInput)

print("Ligand info:")
print("============")
print(dockInput.ligand)

print("Receptor info:")
print("==============")
print(dockInput.receptor)
