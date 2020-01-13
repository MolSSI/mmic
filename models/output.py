from qcelemental import models
from typing import List, Optional

class Output(models.ProtoModel):
        Poses: List[models.Molecule]
        Scores: Optional[List[float]] = None
