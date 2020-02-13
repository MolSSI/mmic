import sys
import abc
sys.path.insert(0, '..')

from base_component.base_component import ProgramHarness
from models.input import DockingInput
from models.output import DockPrepOutput

from typing import Any, Dict, List, Optional, Tuple


class DockSimPrepComponent(ProgramHarness, abc.ABC):

    @classmethod
    def input(cls):
        return DockingInput

    @classmethod
    def output(cls):
        return DockingPrepOutput

    def found(raise_error: bool = False) -> bool:
        """
        Checks if the program can be found.
        Parameters
        ----------
        raise_error : bool, optional
            If True, raises an error if the program cannot be found.
        Returns
        -------
        bool
            Returns True if the program was found, False otherwise.
        """
    
    ## Computers

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

    def parse_output(self, outfiles: Dict[str, str], input_model: "DockingInput") -> "DockPrepOutput":
        raise ValueError("parse_output is not implemented for {}.", self.__class__)  