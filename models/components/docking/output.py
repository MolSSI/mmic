from typing import List, Optional, Tuple, Union
from .input import DockingInput
from models.domains.docking.molecule import MMolecule
from qcelemental import models

class DockingOutput(models.ProtoModel):
    dockingInput: DockingInput
    poses: List[MMolecule]
    flexible: Optional[List[MMolecule]] = None
    scores: Optional[List[float]] = None

class DockingSimOutput(models.ProtoModel):
    pass