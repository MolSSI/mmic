from ..input import DockingInput
from ..output import DockingSimOutput
from models.molecmech.molecules.mm_molecule import MMolecule

from qcelemental import models
from typing import List, Optional, Tuple, Union
from pydantic import Field

class AutoDockSimOutput(DockingSimOutput):
    pass
