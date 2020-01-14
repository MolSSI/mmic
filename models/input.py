from qcelemental import models
from typing import List, Optional, Tuple

class DockingInputData(models.ProtoModel):
    LigandPath: str
    ReceptorPath: str

class DockingInput(models.ProtoModel):
    Ligand: models.Molecule
    Receptor: models.Molecule
    Solvent: Optional[models.Molecule] = None
    Ions: Optional[models.Molecule] = None

class Simulation(models.ProtoModel):
    SearchBox: Optional[List[Tuple[float]]] = None