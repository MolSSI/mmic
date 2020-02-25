from qcelemental import models
from typing import List, Optional, Any, Dict
import os
from rdkit import Chem
from pydantic import validator

from rdkit import rdBase
rdBase.DisableLog('rdApp.error')


class _codesSupported:
    codes = ('Smiles', 'Smarts', 'Inchi', 'FASTA', 'HELM', 'Sequence')

class ChemCode(models.ProtoModel):
    code: str

    @validator('code')
    def validCode(cls, v):
        for code in _codesSupported.codes:
            function = getattr(Chem, f"MolFrom{code}")(v)
            if function:
                break
        return v

class Identifiers(models.molecule.Identifiers):
    smarts: Optional[ChemCode] = None
    sequence: Optional[ChemCode] = None
    fasta: Optional[ChemCode] = None
    helm: Optional[ChemCode] = None

class MMolecule(models.Molecule):
    residues: Optional[Dict[str, List[int]]] = None
    chains: Optional[Dict[str, List[int]]] = None
    segments: Optional[Dict[str, List[int]]] = None
    identifiers: Optional[Identifiers] = None