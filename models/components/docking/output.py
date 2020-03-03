from typing import List, Optional, Tuple, Union
from .input import DockingInput
from models.domains.docking.molecule import MMolecule
from qcelemental import models
from pydantic import Field

class DockingOutput(models.ProtoModel):
    dockingInput: DockingInput = Field(..., description="Docking input model.")
    poses: List[MMolecule] = Field(..., description="Orientation of the ligand relative to the receptor as well as the conformation of the candidate ligand.")
    flexible: Optional[List[MMolecule]] = Field(None, description="Orientation of the flexible side chains of the receptor relative to the ligand.")
    scores: Optional[List[float]] = Field(None, description="A metric for evaluating a particular pose. Length of scores must be equal to length of poses.")

class DockingSimOutput(models.ProtoModel):
    pass