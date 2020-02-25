import sys

from qcelemental import models
from components.blueprints.utils.convert_component import ConvertComponent
from typing import Any, Dict, List, Optional, Tuple
from qcelemental import models

from models.components.docking.input import DockingInput, DockingPrepInput
from models.domains.docking.molecule import MMolecule

from Bio.PDB import PDBParser

class ConvertAutoDockComponent(ConvertComponent):

    @classmethod
    def input(cls):
        return DockingPrepInput

    @classmethod
    def output(cls):
        return DockingInput

    def build_input(
        self, input_model: models.ProtoModel, config: "TaskConfig" = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        raise ValueError("build_input is not implemented for {}.", self.__class__)

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        ligand = MMolecule(symbols=['H'], geometry=[0.0, 0.0, 0.0], identifiers={'smiles': inputs.ligand.code})

        parser = PDBParser()

        filename = inputs.receptor.path.split('/')[-1]
        struct_name = filename.split('.')[0]
        structure = parser.get_structure(struct_name, inputs.receptor.path)
        symb = []
        geom = []
        
        for atom in structure.get_atoms():
            symb.append(atom.element)
            atom_x, atom_y, atom_z = atom.get_coord()
            geom.append(atom_x)
            geom.append(atom_y)
            geom.append(atom_z)

        receptor = MMolecule(symbols=symb, geometry=geom, extras={'filename':inputs.receptor.path, 'removeResidues': ['HOH']})

        return True, DockingInput(ligand=ligand, receptor=receptor)

    def parse_input(self):
        pass
