from typing import List, Optional, Tuple, Union
from qcelemental import models
from models.domains.docking.molecule import MMolecule
from models.domains.classmech.molecule import ChemCode
from models.components.utils.input import FileInput


class DockingInput(models.ProtoModel):
    ligand: MMolecule
    receptor: MMolecule
    searchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = None

class DockingPrepInput(DockingInput):
    ligand: Union[ChemCode, FileInput, MMolecule]
    receptor: Union[FileInput, MMolecule]
    flexible: Optional[Union[MMolecule, FileInput]] = None

class DockingSimInput(models.ProtoModel):
    dockingInput: DockingInput
    ligand: Union[List[str], List[MMolecule]]
    receptor: Union[str, MMolecule]
    rotLigBonds: Optional[List[Tuple[int, int]]] = None 
    rotRecBonds: Optional[List[Tuple[int, int]]] = None
    searchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = None