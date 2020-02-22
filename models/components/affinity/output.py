from qcelemental import models
from ..docking import DockingOutput

class AffinityOutput(models.ProtoModel):
    Docking_Output: DockingOutput
    Affinity: float