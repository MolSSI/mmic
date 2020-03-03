from qcelemental import models

try:
    from rdkit import Chem
except:
    raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')

class RDKitMolecule(models.ProtoModel):
    mol: Chem.rdchem.Mol = None

    class Config:
        arbitrary_types_allowed = True