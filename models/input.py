from qcelemental import models
from typing import List, Optional


class DockingInputData(models.ProtoModel):
    LigandPath: str
    ProteinPath: str
    SearchBox: Optional[List[float]] = None
    

class DockingInput(models.ProtoModel):
	Ligand: models.Molecule
	Receptor: models.Molecule
	SearchBox: Optional[List[float]] = None
