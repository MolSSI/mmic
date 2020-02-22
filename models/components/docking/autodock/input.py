from typing import List, Optional, Tuple, Union
from models.domains.docking.molecule import MMolecule
from ..input import DockingInput, DockingSimInput

class AutoDockSimInput(DockingSimInput):
    Docking_Input: DockingInput
    Exhaustiveness: Optional[int] = 8
    Seed: Optional[int] = None
    BindingModes: Optional[int] = 9
    EnergyRange: Optional[int] = 3 # in kcal/mol
    NumProc: Optional[int] = None