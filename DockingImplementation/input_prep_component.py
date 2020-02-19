import sys
sys.path.insert(0, '..')
from DockingBlueprints.docking_input_component import DockingInputPrepComponent
from models.input import DockingInput
from config import TaskConfig
from models.molecule import MMolecule
import os
from typing import Dict, Any, Tuple, Optional, List

from Bio.PDB import *

class MolSSIInputPrep(DockingInputPrepComponent):

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        ligand = MMolecule(symbols=['H'], geometry=[0.0, 0.0, 0.0], identifiers={'smiles': inputs.Ligand})

        parser = PDBParser()
        filename = inputs.Receptor.split('/')[-1]
        struct_name = filename.split('.')[0]
        structure = parser.get_structure(struct_name, inputs.Receptor)
        symb = []
        geom = []
        
        for atom in structure.get_atoms():
            symb.append(atom.element)
            atom_x, atom_y, atom_z = atom.get_coord()
            geom.append(atom_x)
            geom.append(atom_y)
            geom.append(atom_z)

        receptor = MMolecule(symbols=symb, geometry=geom, extras={'pdbfname':inputs.Receptor})

        return True, DockingInput(Ligand=ligand, Receptor=receptor)
