from typing import Any, Dict, List, Optional, Tuple
from models.input import DockingInputData, DockingInput
from config import TaskConfig

@contextmanager
def tempcd(*args, **kwargs):
    cur = os.getcwd()
    try:
        with temporary_directory(*args, **kwargs) as tmpdir:
            os.chdir(tmpdir)
            yield
    finally:
        os.chdir(cur)
        
class AutoDock(DockingComponent):
    
    def compute(cls, input_data: DockingInput, config: TaskConfig) -> "DockingOutput":
        dict = build_input()
        
    def found(raise_error: bool = False) -> bool:
        raise NotImplementedError

    def build_input(
        self, input_model: DockingInput, config: TaskConfig, template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        receptor = input_model.receptor
        ligand = input_model.ligand

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