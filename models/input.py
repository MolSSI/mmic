from qcelemental import models
from typing import List, Optional, Tuple, Union
from models.molecule import MMolecule

class DockingInputData(models.ProtoModel):
    Ligand: Union[MMolecule, str]
    Receptor: Union[MMolecule, str]
    BindingSite: Optional[Union[List[Tuple[float, float, float]], str]] = None

class DockingInput(models.ProtoModel):
    Ligand: MMolecule
    Receptor: MMolecule
    BindingSite: Optional[List[Tuple[float]]] = None

class CmdInput(models.ProtoModel):
    Input: Union[str, List[str]]
    Output: Optional[str] = None
    Args: Optional[List[str]] = None

class OpenBabelInput(CmdInput):
    OutputExt: str
    
class GrepInput(CmdInput):
    Pattern: str

class DockingSimInput(models.ProtoModel):
    Ligand: Union[str, MMolecule]
    Receptor: Union[str, MMolecule]
    Exhaustiveness: Optional[int] = None
    Seed: Optional[int] = None
    SearchSpace: Optional[Tuple[float, float, float, float, float, float]] = None