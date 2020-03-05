import sys
import abc

from components.base.base_component import ProgramHarness
from models.components.docking.input import DockingInput, DockingSimInput
from models.molecmech.molecules.mm_molecule import MMolecule

from typing import Any, Dict, List, Optional, Tuple
import random
import string

class DockSimPrepComponent(ProgramHarness, abc.ABC):

    @classmethod
    def input(cls):
        return DockingInput

    @classmethod
    def output(cls):
        return DockingSimInput

    def found(raise_error: bool = False) -> bool:
        """
        Checks if the program can be found.
        Parameters
        ----------
        raise_error : bool, optional
            If True, raises an error if the program cannot be found.
        Returns
        -------
        bool
            Returns True if the program was found, False otherwise.
        """
    
    ## Computers

    def build_input(
        self, input_model: "DockingInput", config: "TaskConfig" = None, template: Optional[str] = None
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
        raise NotImplementedError("execute is not implemented for {}.", self.__class__)

    def parse_output(self, outfiles: Dict[str, str], input_model: "DockingInput") -> "DockPrepOutput":
        raise NotImplementedError("parse_output is not implemented for {}.", self.__class__)

    # helper functions
    def receptor_prep(self, receptor: MMolecule) -> Any:
        raise NotImplementedError(f"receptor_prep is not implemented for {self.__class__}.")

    def ligand_prep(self, receptor: MMolecule) -> Any:
        raise NotImplementedError(f"ligand_prep is not implemented for {self.__class__}.")

    @staticmethod
    def randomString(stringLength=10) -> str:
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(stringLength))
