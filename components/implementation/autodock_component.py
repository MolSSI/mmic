from typing import Any, Dict, List, Optional, Tuple
from models.components.docking.autodock.input import AutoDockSimInput
from models.component.docking.autodock.output import AutoDockOutput
from blueprints.docking_sim_component import DockSimComponent

class AutoDock(DockSimComponent):
    
    @classmethod
    def input(cls):
        return DockingSimInput

    @classmethod
    def output(cls):
        return DockingOutput

    def build_input(
        self, input_model: "DockingInput", config: "TaskConfig" = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        raise ValueError("build_input is not implemented for {}.", self.__class__)

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        raise ValueError("execute is not implemented for {}.", self.__class__)

    def parse_output(self, outfiles: Dict[str, str], input_model: "DockingInput") -> "DockingOutput":
        raise ValueError("parse_output is not implemented for {}.", self.__class__)
