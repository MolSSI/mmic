import sys
sys.path.insert(0, '..')

from models.components.docking.input import DockingPrepInput
from models.components.utils.input import OpenBabelInput
from models.components.utils.input import GrepInput
import numpy
import os

# Test MMolecule
from models.domains.docking.molecule import MMolecule

# Test input file
pdb_file = os.path.abspath('../data/dialanine/dialanine.pdb')

docking_input_data = DockingPrepInput(
			Ligand='CCC',
			Receptor=pdb_file
		)

from components.implementation.openbabel_component import OpenBabel
from components.implementation.grep_component import Grep
from components.implementation.autodock_prep_component import AutoDockPrep
from components.implementation.input_prep_component import MolSSIInputPrep

from config import TaskConfig


# Test MolSSIInputPrep
docking_input = MolSSIInputPrep.compute(docking_input_data)

# Test for openbabel
obabel_input = OpenBabelInput(Input=pdb_file, OutputExt='pdbqt')
obabel_output = OpenBabel.compute(obabel_input)
print("==============================")
print("OBABEL OUTPUT:")
print("==============================")
print(obabel_output.Contents)

# Test for grep
grep_input = GrepInput(Input=pdb_file, Pattern='ATOM')
grep_output = Grep.compute(grep_input)
print("==============================")
print("GREP OUTPUT:")
print("==============================")
print(grep_output.Contents)

# Test for AutodockPrep
ADP = AutoDockPrep.compute(input_data=docking_input)

