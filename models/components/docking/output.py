from typing import List, Optional, Tuple, Union
from .input import DockingInput
from models.molecule import MMolecule
from qcelemental import models

class DockingOutput(models.ProtoModel):
    Docking_Input: DockingInput
    Poses: List[MMolecule]
    Flexible: Optional[List[MMolecule]] = None
    Scores: Optional[List[float]] = None

class DockingSimOutput(models.ProtoModel):
    pass