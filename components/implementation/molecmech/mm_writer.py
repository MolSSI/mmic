try:
    from rdkit import rdBase, Chem
    from rdkit.Chem import AllChem
except:
    raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')

from components.blueprints.generic_component import GenericComponent
from models.components.utils.output import FileOutput


class MMoleculeWriter(GenericComponent):

    @classmethod
    def input(cls):
        return MMolecule

    @classmethod
    def output(cls):
        return FileOutput