import sys

from qcelemental import models
from components.blueprints.generic_component import GenericComponent
from typing import Any, Dict, List, Optional, Tuple
from qcelemental import models

from models.components.docking.input import DockingInput, DockingPrepInput
from models.molecmech.molecules.mm_molecule import MMolecule
from models.molecmech.chem.codes import ChemCode
from models.components.utils.input import FileInput

class MMConstructorComponent(GenericComponent):

    @classmethod
    def input(cls):
        return models.ProtoModel

    @classmethod
    def output(cls):
        return MMolecule

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        return True, self.constructor(inputs)

    def constructor(self, model: models.ProtoModel) -> MMolecule:
        if isinstance(model, ChemCode):
            ctype = str(model.codeType).lower()
            return MMolecule(symbols=['C'], geometry=[0,0,0], identifiers={ctype: model})
        elif isinstance(model, FileInput):
            return MMolecule.from_file(model.path)
        elif isinstance(model, MMolecule):
            return model
        else:
            raise ValueError(f'Input type {type(model)} not supported for {self.__class__}')
