from ..base.base_component import ProgramHarness
from cmselemental.models import ProtoModel
from cmselemental.util.decorators import classproperty

__all__ = ["GenericComponent"]


class GenericComponent(ProgramHarness):
    @classproperty
    def input(cls):
        return ProtoModel

    @classproperty
    def output(cls):
        return ProtoModel

    @staticmethod
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
        raise NotImplementedError
