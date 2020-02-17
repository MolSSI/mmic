import sys
sys.path.insert(0, '..')

from models import input
from qcelemental.models import Molecule, ProtoModel

class DockingInputData(ProtoModel):
    Ligand: Molecule


ligand = Molecule(symbols=['H'], geometry=[0.0, 0.0, 0.0], identifiers={'smiles': 'CCC'})

docking_input_data = DockingInputData(Ligand=ligand)

DockingInputData(**docking_input_data.dict())
