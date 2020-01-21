from qcelemental import models
from typing import List, Optional, Tuple, Union

class DockingInputData(models.ProtoModel):
    Ligand: Union[models.Molecule, str]
    Receptor: Union[models.Molecule, str]
    BindingSite: Optional[Union[List[Tuple[float, float, float]], str]] = None

class DockingInput(models.ProtoModel):
    Ligand: models.Molecule
    Receptor: models.Molecule
    BindingSite: Optional[List[Tuple[float]]] = None

class CmdInput(models.ProtoModel):
    Input: str
    Args: Optional[List[str]]

class OpenBabelInput(CmdInput):
    OutputExt: str
    InputExt: Optional[str]
    
class GrepInput(CmdInput):
    Pattern: str
