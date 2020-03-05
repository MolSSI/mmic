from components.implementation.molecmech.mm_constructor import MMConstructorComponent
from typing import Any, Dict, List, Optional, Tuple

from models.components.docking.input import DockingInput, DockingPrepInput
from models.molecmech.molecules.mm_molecule import MMolecule

class ConvertAutoDockComponent(MMConstructorComponent):

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

        ligand = self.constructor(inputs.ligand)
        receptor = self.constructor(inputs.receptor)

        return True, DockingInput(ligand=ligand, receptor=receptor)