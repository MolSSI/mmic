from components.blueprints.docking.docking_component import DockingComponent
from components.implementation.docking.autodock_prep_component import AutoDockPrepComponent
from components.implementation.docking.autodock_sim_component import AutoDockSimComponent
from components.implementation.docking.autodock_post_component import AutoDockPostComponent

from typing import Any, Dict, List, Optional, Tuple

class AutoDockComponent(DockingComponent):

    def execute(self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None
    ) -> Tuple[bool, Dict[str, Any]]:

        simInput   = AutoDockPrepComponent.compute(input_data=inputs)
        simOutput  = AutoDockSimComponent.compute(input_data=simInput)
        dockOutput = AutoDockPostComponent.compute(input_data=simOutput)

        return True, dockOutput