from typing import List, Optional, Tuple, Union
from qcelemental import models
from models.domains.docking.molecule import MMolecule

class DockingInput(models.ProtoModel):
    Ligand: MMolecule
    Receptor: MMolecule
    RotLigBonds: Optional[List[Tuple[int, int]]] = None 
    RotRecBonds: Optional[List[Tuple[int, int]]] = None
    SearchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = None

class DockingPrepInput(DockingInput):
    Ligand: Union[MMolecule, str]
    Receptor: Union[MMolecule, str]
    Flexible: Optional[Union[MMolecule, str]] = None


class DockingSimInput(models.ProtoModel):
    Docking_Input: DockingInput
    Ligand: Union[List[str], List[MMolecule]]
    Receptor: Union[str, MMolecule]
    RotLigBonds: Optional[List[Tuple[int, int]]] = None 
    RotRecBonds: Optional[List[Tuple[int, int]]] = None
    SearchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = None