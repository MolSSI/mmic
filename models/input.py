from qcelemental import models
from typing import List, Optional

class Docking(models.ProtoModel):
	Ligand: models.Molecule
	Receptor: models.Molecule
	SearchBox: Optional[List[float]] = None
