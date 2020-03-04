import qcelemental
from typing import List, Tuple, Optional, Any, Dict, Union
import os, sys
import random
import string
import numpy
from pydantic import validator, Field, ValidationError
from components.implementation.utils.mm_reader import MMoleculeReader, MMoleculeReaderInput
from models.tools.rdkit.codes import ChemCode
from models.components.utils.input import FileInput
from pathlib import Path

class Identifiers(qcelemental.models.molecule.Identifiers):
    smarts: Optional[ChemCode] = None
    sequence: Optional[ChemCode] = None
    fasta: Optional[ChemCode] = None
    helm: Optional[ChemCode] = None

class MMolecule(qcelemental.models.Molecule):

    rotateBonds: Optional[List[Tuple[int, int]]] = Field(None, description="A list of bonded atomic indices: (atom1, atom2), specifying rotatable bonds in the molecule.")
    rigidBonds: Optional[List[Tuple[int, int]]] = Field(None, description="A list of bonded atomic indices: (atom1, atom2), specifying rigid bonds in the molecule.")
    residues: Optional[List[Tuple[str, int]]] = Field(None, description="A list of (residue_name, residue_num) of connected atoms constituting the building block (monomer) of a polymer. Order "
        " follows atomic indices from 0 till Natoms-1. E.g. ('ALA', 1) means atom 0 belongs to aminoacid alanine with residue number 1. Residue number >= 1.")
    chains: Optional[Dict[str, List[int]]] = Field(None, description="A sequence of connected residues.")
    segments: Optional[Dict[str, List[int]]] = Field(None, description="A 2D list of atomic indices specifying which bonds in the ligand are rotatable.")
    identifiers: Optional[Identifiers] = Field(None, description="An optional dictionary of additional identifiers by which this MMolecule can be referenced, "
        "such as INCHI, SMILES, SMARTs, etc. See the :class:``Identifiers`` model for more details.")
    names: Optional[List[str]] = Field(None, description="A list of atomic label names.")

    # Constructors
    @classmethod
    def from_file(cls, filename: str, dtype: Optional[str] = None, *, orient: bool = False, **kwargs) -> "MMolecule":
        """
        Constructs a molecule object from a file.
        Parameters
        ----------
        filename : str
            The filename to build
        dtype : Optional[str], optional
            The type of file to interpret.
        orient : bool, optional
            Orientates the molecule to a standard frame or not.
        **kwargs
            Any additional keywords to pass to the constructor
        Returns
        -------
        Molecule
            A constructed molecule class.
        """
        ext = Path(filename).suffix

        if not dtype:
            if ext in MMoleculeReader._extension_map:
                dtype = MMoleculeReader._extension_map[ext]
            else:
                return qcelemental.models.molecule.Molecule.from_file(filename, dtype, orient=orient, **kwargs)
        
        if dtype == "pdb":
            pdbFile = MMoleculeReaderInput(file=FileInput(path=filename))
            rdkMol =  MMoleculeReader.compute(pdbFile)
            return cls.from_data(rdkMol, dtype='rdkit')
        else:
            return qcelemental.models.molecule.from_file(filename, dtype, orient=orient, **kwargs)

    @classmethod
    def from_data(cls, data: Union[str, Dict[str, Any], numpy.array, bytes], dtype: Optional[str] = None, *,
        orient: bool = False, validate: bool = None, **kwargs: Dict[str, Any]) -> "MMolecule":
        """
        Constructs a molecule object from a data structure.
        Parameters
        ----------
        data: Union[str, Dict[str, Any], numpy.array]
            Data to construct Molecule from
        dtype: Optional[str], optional
            How to interpret the data, if not passed attempts to discover this based on input type.
        orient: bool, optional
            Orientates the molecule to a standard frame or not.
        validate: bool, optional
            Validates the molecule or not.
        **kwargs: Dict[str, Any]
            Additional kwargs to pass to the constructors. kwargs take precedence over data.
        Returns
        -------
        Molecule
            A constructed molecule class.
        """
        if dtype == "rdkit":
            try:
                from rdkit import Chem
                from models.tools.rdkit.molecule import RDKitMolecule, Bond
            except:
                raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')
            assert isinstance(data, RDKitMolecule)

            symbs = [atom.GetSymbol() for atom in data.mol.GetAtoms()]
            residues = [(atom.GetPDBResidueInfo().GetResidueName(), 
                        atom.GetPDBResidueInfo().GetResidueNumber()) 
                        for atom in data.mol.GetAtoms()]
            names = [atom.GetPDBResidueInfo().GetName() for atom in data.mol.GetAtoms()]

            connectivity = []

            for bond in data.mol.GetBonds():
                bondOrder = Bond.orders.index(bond.GetBondType())
                connectivity.append((bond.GetBeginAtomIdx(), bond.GetEndAtomIdx(), bondOrder))

            geo = data.mol.GetConformer(0).GetPositions()

            input_dict = {'symbols': symbs, 
                          'geometry': geo, 
                          'residues': residues, 
                          'connectivity': connectivity,
                          'names': names}
        else:
            return qcelemental.models.molecule.Molecule.from_data(data, dtype, orient=orient, validate=validate, **kwargs)

        input_dict.update(kwargs)

        return cls(orient=orient, validate=validate, **input_dict)

    def to_file(self, filename: str, dtype: Optional[str] = None) -> None:
        """Writes the Molecule to a file.
        Parameters
        ----------
        filename : str
            The filename to write to
        dtype : Optional[str], optional
            The type of file to write, attempts to infer dtype from the filename if not provided.
        """
        ext = Path(filename).suffix

        if not dtype:
            if ext in MMoleculeReader._extension_map:
                dtype = MMoleculeReader._extension_map[ext]
            else:
                qcelemental.models.molecule.Molecule.to_file(filename, dtype)

        if dtype == 'pdb':
            try:
                from rdkit import Chem
                from models.tools.rdkit.molecule import MMToRDKit
            except:
                raise ModuleNotFoundError('Make sure rdkit is installed for code validation.')
            writer = Chem.PDBWriter(filename)
            rdkmol = MMToRDKit.convert(self)
            writer.write(rdkmol)
            writer.close()