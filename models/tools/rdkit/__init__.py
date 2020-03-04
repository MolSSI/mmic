try:
    from rdkit import Chem
except:
    raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')

from . import molecule
from . import codes
