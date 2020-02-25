import sys

from qcelemental import models
from components.base.base_component import ProgramHarness
from typing import Any, Dict, List, Optional, Tuple
from qcelemental import models

from models.components.utils.input import FileInput

class ReaderComponent(ProgramHarness):

    @classmethod
    def input(cls):
        return FileInput

    @classmethod
    def output(cls):
        return models.ProtoModel

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

    def build_input(
        self, input_model: models.ProtoModel, config: "TaskConfig" = None, template: Optional[str] = None
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


    def parse_output(self, outfiles: Dict[str, str], input_model: models.ProtoModel) -> models.ProtoModel:
        raise ValueError("parse_output is not implemented for {}.", self.__class__)
