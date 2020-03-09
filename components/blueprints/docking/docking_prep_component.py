from components.base.base_component import ProgramHarness
from models.components.docking.input import DockingInput, DockingComputeInput
from models.molecmech.molecules.mm_molecule import MMolecule

from typing import Any
import random
import string

class DockPrepComponent(ProgramHarness):
    """ Preprocessing component for docking. """
    @classmethod
    def input(cls):
        return DockingInput

    @classmethod
    def output(cls):
        return DockingComputeInput

    # helper functions
    def receptor_prep(self, receptor: MMolecule) -> Any:
        raise NotImplementedError(f"receptor_prep is not implemented for {self.__class__}.")

    def ligand_prep(self, receptor: MMolecule) -> Any:
        raise NotImplementedError(f"ligand_prep is not implemented for {self.__class__}.")

    @staticmethod
    def randomString(stringLength=10) -> str:
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(stringLength))
