from components.base.base_component import ProgramHarness
from models.components.docking.output import DockingOutput, DockingSimOutput
from models.molecmech.molecules.mm_molecule import MMolecule

from typing import Any
import random
import string

class DockPostComponent(ProgramHarness):

    @classmethod
    def input(cls):
        return DockingSimOutput

    @classmethod
    def output(cls):
        return DockingOutput

    # helper functions
    def receptor_prep(self, receptor: MMolecule) -> Any:
        raise NotImplementedError(f"receptor_prep is not implemented for {self.__class__}.")

    def ligand_prep(self, receptor: MMolecule) -> Any:
        raise NotImplementedError(f"ligand_prep is not implemented for {self.__class__}.")