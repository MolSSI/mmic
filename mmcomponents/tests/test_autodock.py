import sys
import os

sys.path.insert(0, os.getcwd())
debug = False

# Import models
from models.components.docking.input import DockingRawInput
from models.components.utils.input import FileInput
from models.molecmech.chem.codes import ChemCode

# Construct docking input
receptor = os.path.abspath('data/dialanine/dialanine.pdb')
ligand = 'CCC'
dockRawInput = DockingRawInput(ligand=ligand, receptor=receptor)

# Import components
from components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent
from components.implementation.docking.autodock_component import AutoDockComponent

# Test for AutoDock Vina
dockInput  = ConvertAutoDockComponent.compute(dockRawInput)
dockOutput = AutoDockComponent.compute(dockInput)

print("Scores: ")
print("========")
print(dockOutput.scores)

print("Poses: ")
print("========")
print(dockOutput.poses)
