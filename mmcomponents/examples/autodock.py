import sys
import os
sys.path.insert(0, os.getcwd())

# Import converter component for autodock vina 
from components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent

# Import docking data model
from models.components.docking.input import DockingRawInput

# Construct docking input
receptor = 'data/dialanine/dialanine.pdb'
ligand = 'CCC' # smiles code for propane
dockRawInput = DockingRawInput(ligand=ligand, receptor=receptor)
dockInput = ConvertAutoDockComponent.compute(dockRawInput)

# Import simulation component for autodock vina 
from components.implementation.docking.autodock_component import AutoDockComponent

# Run autodock vina
dockOutput = AutoDockComponent.compute(dockInput)

# Extract output
scores, poses = dockOutput.scores, dockOutput.poses

print("Scores: ")
print("========")
print(dockOutput.scores)

print("Poses: ")
print("========")
print(dockOutput.poses)
