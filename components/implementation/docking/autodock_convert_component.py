import sys

from qcelemental import models
from components.blueprints.utils.convert_component import ConvertComponent
from typing import Any, Dict, List, Optional, Tuple
from qcelemental import models

from models.components.docking.input import DockingInput, DockingPrepInput
from models.domains.classmech.molecule import MMolecule

class ConvertAutoDockComponent(ConvertComponent):

    @classmethod
    def input(cls):
        return DockingPrepInput

    @classmethod
    def output(cls):
        return DockingInput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        ligand = MMolecule(symbols=['C'], geometry=[0,0,0], identifiers={'smiles': inputs.ligand.code})
        receptor = MMolecule.from_file(inputs.receptor.path)

        return True, DockingInput(ligand=ligand, receptor=receptor)

    def parse_input(self):
        pass
