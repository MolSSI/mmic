from qcelemental import models
from typing import List, Optional, Any
import pymol

import random
import string
import os

class MMolecule(models.Molecule):

    def __init__(self, **args):
        """ Initializes params for pymol 1st if a pdb filename is supplied """

        if 'extras' in args:
            if 'pdbfname' in args['extras']:

                pdbfname = args['extras']['pdbfname']

                pymol.cmd.set('retain_order', 1)
                pymol.cmd.set('pdb_use_ter_records', 0)

                pymol.cmd.load(pdbfname)

        super().__init__(**args)

    @staticmethod
    def randomString(stringLength=10) -> str:
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(stringLength))

    def write_pdb(self, pdbfname):
        pymol.cmd.save(pdbfname)

    def clear_pdb(self):
        pymol.cmd.delete(self.extras['pdbfname'])