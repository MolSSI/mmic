from qcelemental import models
from typing import List, Optional
from .input import DockingInput

class DockingOutput(models.ProtoModel):
    Docking_Input: DockingInput
    Poses: List[models.Molecule]
    Scores: Optional[List[float]] = None

class Affinity(models.ProtoModel):
    Affinity: float
