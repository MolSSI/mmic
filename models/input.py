from qcelemental import models
from typing import List, Optional, Tuple, Union
from models.molecule import MMolecule

class DockingInputData(models.ProtoModel):
    Ligand: Union[MMolecule, str]
    Receptor: Union[MMolecule, str]
    BindingSite: Optional[Union[List[Tuple[float, float, float]], str]] = None
    Flexible: Optional[Union[MMolecule, str]] = None

class DockingInput(models.ProtoModel):
    Ligand: MMolecule
    Receptor: MMolecule
    BindingSite: Optional[List[Tuple[float]]] = None
    Flexible: Optional[MMolecule] = None

class CmdInput(models.ProtoModel):
    Input: Union[str, List[str]]
    Output: Optional[str] = None
    Args: Optional[List[str]] = None

class OpenBabelInput(CmdInput):
    OutputExt: str
    
class GrepInput(CmdInput):
    Pattern: str

class DockingSimInput(models.ProtoModel):
    # Basic attr
    Ligand: Union[str, MMolecule]
    Receptor: Union[str, MMolecule]

    # Sim params
    Exhaustiveness: Optional[int] = 8
    Seed: Optional[int] = None
    BindingModes: Optional[int] = 9
    EnergyRange: Optional[int] = 3 # in kcal/mol
    NumProc: Optional[int] = None
    SearchSpace: Optional[Tuple[float, float, float, float, float, float]] = None

    # Flexible substructures (e.g. side chains)