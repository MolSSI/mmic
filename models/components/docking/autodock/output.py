from ..input import DockingInput
from ..output import DockingSimOutput
from models.domains.docking.molecule import MMolecule

from qcelemental import models
from typing import List, Optional, Tuple, Union

class AutoDockPostOutput(DockingInput):
    Docking_Input: DockingInput
    Ligand: Union[MMolecule, str]
    Receptor: Union[MMolecule, str]
    Scores: List[float]
    Poses: List[Union[MMolecule, str]]
    Flexible: Optional[Union[MMolecule, str]] = None

class AutoDockSimOutput(DockingSimOutput):
    pass