import abc
from typing import Any, Dict, List, Optional, Tuple

import sys
sys.path.insert(0, '..')
from config import TaskConfig

from qcelemental import models

class ProgramHarness(models.ProtoModel, abc.ABC):

    _defaults: Dict[str, Any] = {}
    name: str
    scratch: bool
    thread_safe: bool
    thread_parallel: bool
    node_parallel: bool
    managed_memory: bool
    extras: Optional[Dict[str, Any]]

    class Config:
        allow_mutation: False
        extra: "forbid"

    def __init__(self, **kwargs):
        super().__init__(**{**self._defaults, **kwargs})

    @classmethod
    def input(cls):
        return models.ProtoModel

    @classmethod
    def output(cls):
        return models.ProtoModel

    @classmethod
    def compute(cls, input_data: models.ProtoModel, config: "TaskConfig" = None) -> models.ProtoModel:
        #Validate the input model

        #print("input types = ", type(input_data), type(cls.input()), models.ProtoModel)

        #if isinstance(input_data, cls.input()):
        #    cls.input()(**input_data.dict())
        #elif isinstance(input_data, dict):
        #    cls.input()(**input_data)
        #else:
        #    raise TypeError("{0} is not a valid input type for the {1} component.".format(type(input_data), cls.__name__))

        #Perform the execution
        program = cls(name = cls.__name__, scratch = False, thread_safe = False, thread_parallel = False, node_parallel = False, managed_memory = False)

        _, exec_output = program.execute(input_data)

        #print("output types = ", type(exec_output[-1]), type(cls.output()))

        #Validate the output model
        #if isinstance(exec_output, cls.output()):
        #    cls.output()(**exec_output.dict())
        #elif isinstance(exec_output, dict):
        #    cls.output()(**exec_output)
        #else:
        #    raise TypeError("{0} is not a valid output type for the {1} component.".format(type(exec_output), cls.__name__))

        return exec_output

    @staticmethod
    @abc.abstractmethod
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

    ## Utility

    def get_version(self) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """

    ## Computers

    @classmethod
    def build_input(
        cls, input_model: models.ProtoModel, config: "TaskConfig" = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        raise ValueError("build_input is not implemented for {}.", self.__class__)

    @classmethod
    def execute(
        cls,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        raise ValueError("execute is not implemented for {}.", self.__class__)

    @classmethod
    def parse_output(cls, outfiles: Dict[str, str], input_model: models.ProtoModel) -> models.ProtoModel:
        raise ValueError("parse_output is not implemented for {}.", self.__class__)
