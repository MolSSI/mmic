from qcelemental import models
from typing import List, Optional, Any
import pymol

import random
import string
import os

class MMolecule(models.Molecule):
    substructures: Optional[List[Any]] = None

    @classmethod
    def store_residues(cls, pdb_file):
        """ Stores residue name from pdb file """
        pymol.cmd.set('retain_order', 1)
        pymol.cmd.set('pdb_use_ter_records', 0)

        pymol.cmd.load(os.path.abspath(pdb_file))
        residues = []

        def get_resn(index, resn):
            residues.append([index, resn])

        myspace = {'get_resn': get_resn}
        pymol.cmd.iterate('(all)', 'get_resn(index, resn)', space=myspace)

        return residues

    @staticmethod
    def randomString(stringLength=10) -> str:
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(stringLength))

    def write_pdb(self, pdbfname):

        filename = os.path.abspath(MMolecule.randomString() + '.xyz')
        self.to_file(filename)

        if self.substructures:
            def set_resn(atom_index):
                pymol.cmd.alter(f'(index {atom_index})', f'resn="{self.substructures[atom_index-1][1]}"')

            pymol.cmd.load(filename)

            myspace = {'set_resn': set_resn}
            pymol.cmd.iterate('(all)', 'set_resn(index)', space=myspace)
            pymol.cmd.save(pdbfname)

        os.remove(filename)