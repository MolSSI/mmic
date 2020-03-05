from components.implementation.molecmech.mm_constructor import MMConstructorComponent
from typing import Any, Dict, List, Optional, Tuple
import os

from models.components.docking.input import DockingInput, DockingRawInput
from models.molecmech.molecules.mm_molecule import MMolecule
from models.components.utils.input import FileInput
from models.molecmech.chem.codes import ChemCode

class ConvertAutoDockComponent(MMConstructorComponent):

    @classmethod
    def input(cls):
        return DockingRawInput

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

        if(os.path.isfile(inputs.ligand)):
            ligand = FileInput(path=inputs.ligand)
        else: # had better be a valid chem code
            ligand = ChemCode(code=inputs.ligand)
        ligand = self.constructor(ligand)

        if(os.path.isfile(inputs.receptor)):
            receptor = FileInput(path=inputs.receptor)
        else: # had better be a valid chem code
            receptor = ChemCode(code=inputs.receptor)
        receptor = self.constructor(receptor)

        return True, DockingInput(ligand=ligand, receptor=receptor)