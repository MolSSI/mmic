import sys
sys.path.insert(0, '..')
from DockingBlueprints.docking_input_component import DockingInputPrepComponent
from models.input import DockingInputData, DockingInput
from config import TaskConfig
from models.molecule import MMolecule
import os

from Bio.PDB import *

class MolSSIInputPrep(DockingInputPrepComponent):
        
    @classmethod
    def compute(cls, input_data: "DockingInputData", config: "TaskConfig" = None) -> "DockingInput":
        ligand = MMolecule(symbols=['H'], geometry=[0.0, 0.0, 0.0], identifiers={'smiles': input_data.Ligand})

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

        if os.path.isfile(input_data.Receptor):
            residues = MMolecule.store_residues(input_data.Receptor)

            receptor = MMolecule(symbols=symb, geometry=geom, substructures=residues)
        else:
            receptor = MMolecule(symbols=symb, geometry=geom)
        
        return DockingInput(Ligand=ligand, Receptor=receptor)