
from rdkit import Chem

from qcelemental import models
from typing import List, Optional, Any, Dict

from components.blueprints.utils.writer_component import WriterComponent

class MMoleculeWriter(WriterComponent):

    @classmethod
    def input(cls):
        return MMolecule

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        pass

    # writer methods
    def writePDB(self, pdbfname):
        writer = Chem.PDBWriter(pdbfname)
        writer.write(self._mol)
        writer.close()

    def writeXYZ(self, xyzfname):
        Chem.rdmolfiles.MolToXYZFile

    def write(self, filename):

        ext = filename.split('.')[-1]

        if ext == 'pdb':
            self.writePDB(filename)
        else:
            raise ValueError(f'Input file format not supported: {ext}')