from typing import List, Optional, Tuple, Union
from models.domains.docking.molecule import MMolecule
from qcelemental import models 

class AutoDockSimInput(models.ProtoModel):
    ligand: str
    receptor: str
    Exhaustiveness: Optional[int] = 8
    Seed: Optional[int] = None
    BindingModes: Optional[int] = 9
    EnergyRange: Optional[int] = 3 # in kcal/mol
    NumProc: Optional[int] = None