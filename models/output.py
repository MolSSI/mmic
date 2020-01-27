from qcelemental import models
from typing import List, Optional, Tuple
from .input import DockingInput

class DockingOutput(models.ProtoModel):
    Docking_Input: DockingInput
    Poses: List[Tuple[models.Molecule, models.Molecule]]
    Scores: Optional[List[float]] = None

class Affinity(models.ProtoModel):
    Docking_Output: DockingOutput
    Affinity: float

class FileOutput(models.ProtoModel):
    Contents: str

class AutoDockPrepOutput(models.ProtoModel):
	Ligand: FileOutput
	Receptor: FileOutput
	BindingSite: Optional[List[Tuple[float]]]

class AutoDockOutput(DockingOutput):
	Log: FileOutput