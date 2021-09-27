from ..base.base_component import ProgramHarness
import abc
from typing import Dict, List, Set, Optional, Any, Tuple, Set
from cmselemental.util.decorators import classproperty
import importlib

__all__ = ["StrategyComponent"]


class StrategyComponent(ProgramHarness):
    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        if hasattr(inputs, "component"):
            if inputs.component:
                if not importlib.util.find_spec(inputs.component):
                    raise ModuleNotFoundError(f"{inputs.component} cannot be imported")
                else:
                    comp_mod = importlib.import_module(inputs.component)
                    return True, comp_mod._mainComponent.compute(inputs)

        if not len(self.installed_comps):
            raise ModuleNotFoundError(
                "No supported component is installed. Solve by installing any of the following components:\n"
                + f"{self.tactic_comps}"
            )

        comp_mod = importlib.import_module(comp)
        return True, comp_mod._mainComponent.compute(inputs)

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

    @classproperty
    def installed_comps(cls) -> List[str]:
        """Returns module spec if it exists.

        Returns
        -------
        list[str]
            Component names that are installed.

        """
        if cls.tactic_comps is None:
            raise NotImplementedError(
                f"No components are available. Solve by installing any of the supported components: {cls.tactic_comps()}."
            )
        return [spec for spec in cls.tactic_comps if importlib.util.find_spec(spec)]

    @abc.abstractproperty
    @classproperty
    def tactic_comps(cls) -> Set[str]:
        """Returns the tactic components this strategy component supports.

        Returns
        -------
        set[str]
            A set of compliant tactic component names.

        """
        ...
