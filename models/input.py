from qcelemental import models
from typing import List, Optional, Tuple, Union
from models.molecule import MMolecule

class DockingInputData(models.ProtoModel):
    Ligand: Union[MMolecule, str]
    Receptor: Union[MMolecule, str]
    BindingSite: Optional[Union[List[Tuple[float, float, float]], str]]

class DockingInput(models.ProtoModel):
    Ligand: MMolecule
    Receptor: MMolecule
    BindingSite: Optional[List[Tuple[float]]]

class CmdInput(models.ProtoModel):
    Input: Union[str, List[str]]
    Args: Optional[List[str]]

class OpenBabelInput(CmdInput):
    OutputExt: str
    InputExt: Optional[str]
    
class GrepInput(CmdInput):
    Pattern: str

class DockingSimInput(models.ProtoModel):
	Exhaustiveness: Optional[int] = None
	Seed: Optional[int] = None
	SearchSpace: Optional[Tuple[float, float, float, float, float, float]] = None