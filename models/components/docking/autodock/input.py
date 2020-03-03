from typing import List, Optional, Tuple, Union
from models.domains.classmech.molecule import MMolecule
from qcelemental import models 

class AutoDockSimInput(models.ProtoModel):
    ligand: str
    receptor: str
    exhaustiveness: Optional[int] = 8
    seed: Optional[int] = None
    num_modes: Optional[int] = 9
    energy_range: Optional[int] = 3 # in kcal/mol
    cpu: Optional[int] = None