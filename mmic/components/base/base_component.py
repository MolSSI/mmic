import abc
from typing import Any, Dict, List, Optional, Tuple
from .config import TaskConfig
from cmselemental.models import ProtoModel
from cmselemental.util.decorators import classproperty


class ProgramHarness(ProtoModel, metaclass=abc.ABCMeta):

    _defaults: Dict[str, Any] = {}
    name: str
    scratch: bool
    thread_safe: bool
    thread_parallel: bool
    node_parallel: bool
    managed_memory: bool
    extras: Optional[Dict[str, Any]]

    class Config:
        allow_mutation = False
        extra = "forbid"

    def __init__(self, **kwargs):
        super().__init__(**{**self._defaults, **kwargs})

    @abc.abstractproperty
    @classproperty
    def input(cls):
        ...

    @abc.abstractproperty
    @classproperty
    def output(cls):
        ...

    @classmethod
    def compute(
        cls,
        input_data: ProtoModel,
        config: Optional[TaskConfig] = None,
        scratch: Optional[bool] = False,
        thread_safe: Optional[bool] = False,
        thread_parallel: Optional[bool] = False,
        node_parallel: Optional[bool] = False,
        managed_memory: Optional[bool] = False,
        extras: Optional[Dict[str, Any]] = None,
    ) -> ProtoModel:

        # Validate the input model
        if isinstance(input_data, cls.input):
            cls.input(**input_data.dict())
        elif isinstance(input_data, dict):
            cls.input(**input_data)
        else:
            raise TypeError(
                f"{type(input_data)} is not a valid input type for the {cls.__name__} component."
            )

        # Perform the execution
        program = cls(
            name=cls.__name__,
            scratch=scratch,
            thread_safe=thread_safe,
            thread_parallel=thread_parallel,
            node_parallel=node_parallel,
            managed_memory=managed_memory,
            extras=extras,
        )

        _, exec_output = program.execute(input_data)

        # Validate the output model
        if isinstance(exec_output, cls.output):
            cls.output(**exec_output.dict())
        elif isinstance(exec_output, dict):
            cls.output(**exec_output)
        else:
            raise TypeError(
                f"{type(exec_output)} is not a valid output type for the {cls.__name__} component."
            )

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
        ...

    ## Utility

    @abc.abstractproperty
    @classproperty
    def version(cls) -> str:
        """Returns distutils-style version string.

        Examples
        --------
        The string ">1.0, !=1.5.1, <2.0" implies any version after 1.0 and before 2.0
        is compatible, except 1.5.1

        Returns
        -------
        str
            Return a dist-utils valid version string.

        """
        ...

    ## Computers
    def build_input(
        self,
        input_model: ProtoModel,
        config: TaskConfig = None,
        template: Optional[str] = None,
    ) -> Dict[str, Any]:
        raise NotImplementedError(
            f"build_input is not implemented for {self.__class__}."
        )

    @abc.abstractmethod
    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        raise NotImplementedError(f"execute is not implemented for {self.__class__}.")

    def parse_output(
        self, outfiles: Dict[str, str], input_model: ProtoModel
    ) -> ProtoModel:
        raise NotImplementedError(
            f"parse_output is not implemented for {self.__class__}."
        )
