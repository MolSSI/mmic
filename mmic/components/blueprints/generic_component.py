from ..base.base_component import ProgramHarness
from cmselemental import models

__all__ = ["GenericComponent"]


class GenericComponent(ProgramHarness):
    @classmethod
    def input(cls):
        return models.ProtoModel

    @classmethod
    def output(cls):
        return models.ProtoModel

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

    @classmethod
    def get_version(cls) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        raise NotImplementedError
