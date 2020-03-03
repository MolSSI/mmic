from typing import List, Optional, Tuple, Union
from .input import DockingInput
from models.domains.classmech.molecule import MMolecule
from qcelemental import models
from pydantic import Field

class DockingOutput(models.ProtoModel):
    dockingInput: DockingInput = Field(..., description="Docking input model.")
    poses: List[MMolecule] = Field(..., description="Conformation and orientation of the candidate ligand relative to the receptor.")
    flexible: Optional[List[MMolecule]] = Field(None, description="Conformation and orientation of the flexible side chains in the receptor relative to the ligand.")
    scores: Optional[List[float]] = Field(None, description="A metric for evaluating a particular pose. Length of scores must be equal to length of poses.")

class DockingSimOutput(models.ProtoModel):
    dockingInput: DockingInput = Field(..., description="Docking input model.")
    ligand: Union[MMolecule, str] = Field(..., description="Molecule model for candidate ligand (e.g. drug).")
    receptor: Union[MMolecule, str] = Field(..., description="Molecule model for receptor (e.g. protein).")
    poses: List[Union[MMolecule, str]] = Field(..., description="Conformation and orientation of the candidate ligand relative to the receptor.")
    flexible: Optional[Union[MMolecule, str]] = Field(None, description="Conformation and orientation of the flexible side chains of the receptor relative to the ligand.")
    scores: List[float] = Field(None, description="A metric for evaluating a particular pose. Length of scores must be equal to length of poses.")