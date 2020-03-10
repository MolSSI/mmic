import sys
import os

sys.path.insert(0, os.getcwd())
debug = False

# Import models
from mmcomponents.models.docking.input import DockingRawInput
from mmelemental.models.util.input import FileInput
from mmelemental.models.chem.codes import ChemCode

# Construct docking input
receptor = os.path.abspath('mmcomponents/data/dialanine/dialanine.pdb')
ligand = 'CCC'
dockRawInput = DockingRawInput(ligand=ligand, receptor=receptor)

# Import components
from mmcomponents.components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent
from mmcomponents.components.implementation.docking.autodock_component import AutoDockComponent

# Test for AutoDock Vina
dockInput  = ConvertAutoDockComponent.compute(dockRawInput)
dockOutput = AutoDockComponent.compute(dockInput)

print("Scores: ")
print("========")
print(dockOutput.scores)

print("Poses: ")
print("========")
print(dockOutput.poses)
