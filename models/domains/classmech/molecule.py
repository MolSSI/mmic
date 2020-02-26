from qcelemental import models
from typing import List, Optional, Any, Dict
import os
from pydantic import validator, ValidationError

try:
    from rdkit import rdBase, Chem
    if not os.environ.get('debugMMC'):
        rdBase.DisableLog('rdApp.error')
    rdkAvail = True
except Exception:
    rdkAvail = False
        
class ChemCode(models.ProtoModel):
    code: str
    codeType_: Optional[str] = None

    class _CodesSupported:
        codes = ('Smiles', 'Smarts', 'Inchi', 'FASTA', 'HELM', 'Sequence')

    class Config:
        allow_mutation = True

    def __init__(self, **args):
        super().__init__(**args)
        self.codeType_ = ChemCode.validCode(args.get('code'))

        if args.get('codeType_'):
            if self.codeType_ != args.get('codeType_'):
                raise ValidationError

        self.Config.allow_mutation = False

    @validator('code')
    def validCode(cls, v):
        if rdkAvail:
            for code in ChemCode._CodesSupported.codes:
                function = getattr(Chem, f"MolFrom{code}")
                if function(v):
                    return code
            raise ValidationError
        else:
            return v

    @property
    def codeType(self):
        return self.codeType_

class _Identifiers(models.molecule.Identifiers):
    smarts: Optional[ChemCode] = None
    sequence: Optional[ChemCode] = None
    fasta: Optional[ChemCode] = None
    helm: Optional[ChemCode] = None

class MMolecule(models.Molecule):
    residues: Optional[Dict[str, List[int]]] = None
    chains: Optional[Dict[str, List[int]]] = None
    segments: Optional[Dict[str, List[int]]] = None
    identifiers: Optional[_Identifiers] = None




