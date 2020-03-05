from models.components.docking.output import DockingOutput
from models.components.affinity.output import AffinityOutput
from base.base_component import ProgramHarness

class DockingAffinityComponent(ProgramHarness):
    
    @classmethod
    def input(cls):
        return DockingOutput

    @classmethod
    def output(cls):
        return AffinityOutput