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

class DockingPrepOutput(models.ProtoModel):
    Ligand: Union[FileOutput, MMolecule]
    Receptor: Union[FileOutput, MMolecule]
    Log: Optional[FileOutput] = None
    Exhaustiveness: Optional[int] = None
    Seed: Optional[int] = None
    SearchSpace: Optional[Tuple[float, float, float, float, float, float]] = None