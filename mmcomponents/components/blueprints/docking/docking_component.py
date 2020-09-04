from mmcomponents.models.components.docking.input import DockingInput
from mmcomponents.models.components.docking.output import DockingOutput
from mmcomponents.components.base.base_component import ProgramHarness

class DockingComponent(ProgramHarness):
    
    @classmethod
    def input(cls):
        return DockingInput

    @classmethod
    def output(cls):
        return DockingOutput
