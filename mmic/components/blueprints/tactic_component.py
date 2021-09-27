from ..base.base_component import ProgramHarness
import abc
from cmselemental.util.decorators import classproperty
from typing import Set

__all__ = ["TacticComponent"]


class TacticComponent(ProgramHarness):
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

    @abc.abstractproperty
    @classproperty
    def strategy_comps(cls) -> Set[str]:
        """Returns the strategy component(s) this (tactic) component is compliant with.
        Returns
        -------
        set[str]
            A set of strategy component names.
        """
        ...
