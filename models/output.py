from qcelemental import models
from typing import List, Optional, Tuple, Union
from .input import DockingInput
from models.molecule import MMolecule

class DockingOutput(models.ProtoModel):
    Docking_Input: DockingInput
    Poses: List[Tuple[models.Molecule, models.Molecule]]
    Scores: Optional[List[float]] = None

class Affinity(models.ProtoModel):
    Docking_Output: DockingOutput
    Affinity: float

class FileOutput(models.ProtoModel):
    Contents: str