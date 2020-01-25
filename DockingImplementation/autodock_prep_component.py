import sys
sys.path.insert(0, '..')

from qcengine.util import temporary_directory, execute
from base_component.base_component import ProgramHarness
from models import input
from models import output

# Import utility components
from DockingImplementation.grep_component import Grep
from DockingImplementation.openbabel_component import OpenBabel

from typing import Any, Dict, List, Optional, Tuple
import os
import pymol

from models.input import DockingInput
from qcelemental.models.molecule import Molecule


class AutoDockPrep(ProgramHarness):


    _defaults = {
        "name": "AutoDockPrep",
        "scratch": False,
        "thread_safe": True,
        "thread_parallel": False,
        "node_parallel": False,
        "managed_memory": True,
    }

    @classmethod
    def compute(cls, input_data: input.DockingInput, config: "TaskConfig" = None) -> output.AutoDockPrepOutput:

        return cls.build_input(input_data)

    @classmethod
    def build_input(cls, input_model: DockingInput, template: Optional[str] = None) -> Dict[str, Any]:
        
        ligand = cls.ligand_prep(smiles = input_model.Ligand)
        receptor = cls.receptor_prep(filename = input_model.Receptor)

        return {
            "ligand": input_model.identifiers['smiles'],
            "receptor": receptor
        }

    @classmethod
    def receptor_prep(cls, filename: str) -> str:
        pymol.cmd.load(filename)
        pymol.cmd.remove('resn HOH')
        pymol.cmd.h_add(selection='acceptors or donors')
        pymol.cmd.save('protein.pdb')
        obabel_input = input.OpenBabelInput(Input=os.path.abspath('protein.pdb'), OutputExt='pdbqt', Args=['-xh'])
        os.remove('protein.pdb')

        return OpenBabel.compute(input_data=obabel_input)

    @classmethod
    def ligand_prep(cls, smiles: str) -> str:

        pdbqt_file = os.path.abspath('tmp.pdbqt')

        with open(pdbqt_file, 'w') as fp:
            fp.write(cls.smi_to_pdbqt(smiles))

        grep_input = input.GrepInput(Input=pdbqt_file, Pattern='ATOM')
        grep_output = Grep.compute(input_data=grep_input)

        os.remove(pdbqt_file)

        return grep_output.FileContents

    @classmethod
    def smi_to_pdbqt(cls, smiles: str) -> str:

        smi_file = os.path.abspath('tmp.smi')

        with open(smi_file, 'w') as fp:
            fp.write(smiles)

        obabel_input = input.OpenBabelInput(Input=smi_file, OutputExt='pdbqt', Args=['--gen3d', '-h'])
        obabel_output = OpenBabel.compute(input_data=obabel_input)

        os.remove(smi_file)

        return obabel_output.FileContents        