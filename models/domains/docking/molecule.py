from qcelemental import models
from typing import List, Optional, Any

import random
import string
import os

from rdkit import Chem
from rdkit.Chem import AllChem

from pydantic import validator


class MMolecule(models.Molecule):

    class Config(models.Molecule.Config):
        allow_mutation = True

    def __init__(self, **args):
        """ Creates an instance of mol """

        super().__init__(**args)

        if 'extras' in args:

            # construct RDKit molecule from a file
            if 'filename' in args['extras']:

                filename = args['extras']['filename']
                ext = filename.split('.')[-1]

                if ext == 'pdb':
                    self.extras['rdkMol'] = Chem.MolFromPDBFile(filename)
                elif ext == 'rdkMol':
                    self.extras['rdkMol'] = Chem.MolFromMolFile(filename)
                elif ext == 'mol2':
                    self.extras['rdkMol'] = Chem.MolFromMol2File(filename)
                elif ext == 'tpl':
                    self.extras['rdkMol'] = Chem.MolFromTPLFile(filename)
                elif ext == 'sdf':
                    mols = Chem.SDMolSupplier(filename)

                    if len(mols) > 1:
                        raise ValueError("SDF file should contain a single molecule")
                    else:
                        self.extras['rdkMol'] = mols[0] # should we support multiple molecules?

                else:
                    raise ValueError(f"Unrecognized file type: {ext}")

            # construct RDKit molecule from identifiers
            elif 'identifiers' in args['extras']:

                ids = args['extras']['identifiers']

                if 'smiles' in ids:
                    smiles = ids['smiles']
                    self.extras['rdkMol'] = Chem.MolFromSmiles(smiles)

                elif 'smarts' in ids:
                    smarts = ids['smarts']
                    self.extras['rdkMol'] = Chem.MolFromSmarts(smarts)

                elif 'inchi' in ids:
                    inchi = ids['inchi']
                    self.extras['rdkMol'] = Chem.MolFromInchi(inchi)

                elif 'sequence' in ids:
                    sequence = ids['sequence']
                    self.extras['rdkMol'] = Chem.MolFromInchi(sequence)

                elif 'fasta' in ids:
                    fasta = ids['fasta']
                    self.extras['rdkMol'] = Chem.MolFromFASTA(fasta)

                elif 'helm' in ids:
                    helm = ids['helm']
                    self.extras['rdkMol'] = Chem.MolFromHELM(helm)

                # Do cleanup if requested
                if 'removeResidues' in args['extras']:
                    self.extras['rdkMol'] = self._removeResidues(args['extras']['removeResidues'])

                self._gen3D()

        self.Config.allow_mutation = False

    def _gen3D(self, nConformers=1):
        """ Generates 3D coords for a 2D molecule. Should be called only when instantiating a Molecule object.

        :note: a single unique molecule is assumed. 
        """
        self.extras['rdkMol'] = Chem.AddHs(self.extras['rdkMol'])
        # create n conformers for molecule
        confIds = AllChem.EmbedMultipleConfs(self.extras['rdkMol'], nConformers)

        # Energy optimize
        for confId in confIds:
            AllChem.UFFOptimizeMolecule(self.extras['rdkMol'], confId=confId)

    def _removeResidues(self, residues: List[str]) -> Chem.rdchem.Mol:
        atoms = self.extras['rdkMol'].GetAtoms()
        RWmol = Chem.RWMol(mol)

        for atom in atoms:
            if atom.GetPDBResidueInfo().GetResidueName() in residues:
                RWmol.RemoveAtom(atom.GetIdx())

        return Chem.Mol(RWmol)     

    # writer methods
    def writePDB(self, pdbfname):
        writer = Chem.PDBWriter(pdbfname)
        writer.write(self.extras['rdkMol'])
        writer.close()

    def writeXYZ(self, xyzfname):
        Chem.rdmolfiles.MolToXYZFile

    def write(self, filename):

        ext = filename.split('.')[-1]

        if ext == 'pdb':
            self.writePDB(filename)
        else:
            raise ValueError(f'Input file format not supported: {ext}')
