import sys
import numpy
import os

sys.path.insert(0, os.getcwd())

debug = False

# import models
from models.components.docking.input import DockingPrepInput
from models.components.docking.autodock.input import AutoDockSimInput
from models.components.utils.input import FileInput, OpenBabelInput, GrepInput
from models.tools.rdkit.codes import ChemCode

# Test input file
receptor = FileInput(path=os.path.abspath('data/dialanine/dialanine.pdb'))
ligand = ChemCode(code='CCC')

dockingInputData = DockingPrepInput(ligand=ligand, receptor=receptor)

# Import components
from components.implementation.utils.openbabel_component import OpenBabel
from components.implementation.utils.grep_component import Grep
from components.implementation.docking.autodock_sim_component import AutoDockSim
from components.implementation.docking.autodock_prep_component import AutoDockPrep
from components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent

# Test for ConvertAutoDockComponent
dockingInput = ConvertAutoDockComponent.compute(dockingInputData)

# Test for openbabel
obabel_input = OpenBabelInput(fileInput=receptor, outputExt='pdbqt')
obabel_output = OpenBabel.compute(obabel_input)

if debug:
	print("==============================")
	print("OBABEL OUTPUT:")
	print("==============================")
	print(obabel_output.Contents)

# Test for grep
grep_input = GrepInput(fileInput=receptor, pattern='ATOM')
grep_output = Grep.compute(grep_input)

if debug:
	print("==============================")
	print("GREP OUTPUT:")
	print("==============================")
	print(grep_output.Contents)

# Test for AutodockPrep
simInput  = AutoDockPrep.compute(input_data=dockingInput)
simOutput = AutoDockSim.compute(input_data=simInput)
