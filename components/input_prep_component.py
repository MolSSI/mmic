import sys
sys.path.insert(0, '..')
from components.docking_input_component import DockingInputPrepComponent
from models.input import DockingInputData, DockingInput
from config import TaskConfig
from qcelemental.models.molecule import Molecule

from Bio.PDB import *

class MolSSIInputPrep(DockingInputPrepComponent):
        
    @classmethod
    def compute(cls, input_data: "DockingInputData", config: "TaskConfig") -> "DockingInput":
        ligand = Molecule(symbols=['H'], geometry=[0.0, 0.0, 0.0], identifiers={'smiles': input_data.Ligand})

        parser = PDBParser()
        filename = input_data.Receptor.split('/')[-1]
        struct_name = filename.split('.')[0]
        structure = parser.get_structure(struct_name, input_data.Receptor)
        symb = []
        geom = []
        
        for atom in structure.get_atoms():
            symb.append(atom.element)
            atom_x = atom.get_coord()[0]
            atom_y = atom.get_coord()[1]
            atom_z = atom.get_coord()[2]
            geom.append(atom_x)
            geom.append(atom_y)
            geom.append(atom_z)
        
        receptor = Molecule(symbols=symb, geometry=geom)
        
        return DockingInput(Ligand=ligand, Receptor=receptor)