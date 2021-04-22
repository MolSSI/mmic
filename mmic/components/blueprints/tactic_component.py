from ..base.base_component import ProgramHarness
import abc

__all__ = ["TacticComponent"]


class TacticComponent(ProgramHarness):
    @classmethod
    @abc.abstractmethod
    def get_version(cls) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        raise NotImplementedError

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
    @abc.abstractmethod
    def strategy_comp(cls) -> str:
        """Returns the strategy component this (tactic) component belongs to.
        Returns
        -------
        Set[str]
        """
        raise NotImplementedError
