import sys
import numpy
import os

sys.path.insert(0, '..')

# import models
from models.components.docking.input import DockingPrepInput
from models.components.utils.input import FileInput, OpenBabelInput, GrepInput
from models.domains.classmech.molecule import ChemCode
from models.domains.docking.molecule import MMolecule

# Test input file
receptor = FileInput(path=os.path.abspath('../data/dialanine/dialanine.pdb'))
ligand = ChemCode(code='CCC')

docking_input_data = DockingPrepInput(ligand=ligand, receptor=receptor)

from components.implementation.utils.openbabel_component import OpenBabel
from components.implementation.utils.grep_component import Grep
from components.implementation.docking.autodock_prep_component import AutoDockPrep
from components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent

from config import TaskConfig

# Test for ConvertAutoDockComponent
docking_input = ConvertAutoDockComponent.compute(docking_input_data)

# Test for openbabel
obabel_input = OpenBabelInput(fileInput=receptor, outputExt='pdbqt')
obabel_output = OpenBabel.compute(obabel_input)
print("==============================")
print("OBABEL OUTPUT:")
print("==============================")
print(obabel_output.Contents)

# Test for grep
grep_input = GrepInput(fileInput=receptor, pattern='ATOM')
grep_output = Grep.compute(grep_input)
print("==============================")
print("GREP OUTPUT:")
print("==============================")
print(grep_output.Contents)

# Test for AutodockPrep
ADP = AutoDockPrep.compute(input_data=docking_input)
