from qcelemental import models
from typing import List, Optional, Tuple

class DockingInputData(models.ProtoModel):
    LigandPath: str
    ReceptorPath: str
    BindingSitePath: Optional[str] = None

class DockingInput(models.ProtoModel):
    Ligand: models.Molecule
    Receptor: models.Molecule
    BindingSite: Optional[List[Tuple[float]]] = None

class OpenBabelInput(models.ProtoModel):
    Input: str
    Output: str
    Args: Optional[List[str]]