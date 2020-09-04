from mmcomponents.components.base.base_component import ProgramHarness
from mmcomponents.models.components.docking.output import DockingOutput, DockingSimOutput
from mmelemental.models.molecmech.molecules.mm_molecule import Molecule

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
    def receptor_prep(self, receptor: Molecule) -> Any:
        raise NotImplementedError(f"receptor_prep is not implemented for {self.__class__}.")

    def ligand_prep(self, receptor: Molecule) -> Any:
        raise NotImplementedError(f"ligand_prep is not implemented for {self.__class__}.")
