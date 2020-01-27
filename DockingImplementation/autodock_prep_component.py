import sys
sys.path.insert(0, '..')

from qcengine.util import temporary_directory, execute
from base_component.base_component import ProgramHarness
from models import input, molecule
from models import output

# Import utility components
from DockingImplementation.grep_component import Grep
from DockingImplementation.openbabel_component import OpenBabel

from typing import Any, Dict, List, Optional, Tuple
import os
import pymol


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

        binput =  cls.build_input(input_data)
        ligand = output.FileOutput(Contents=binput['ligand'])
        receptor = output.FileOutput(Contents=binput['receptor'])
        return output.AutoDockPrepOutput(Ligand=ligand, Receptor=receptor)

    @classmethod
    def build_input(cls, input_model: input.DockingInput, template: Optional[str] = None) -> Dict[str, Any]:

        ligand = cls.ligand_prep(smiles = input_model.Ligand.identifiers.smiles)
        receptor = cls.receptor_prep(receptor = input_model.Receptor)

        return {
            "ligand": ligand,
            "receptor": receptor
        }

    @classmethod
    def receptor_prep(cls, receptor: molecule.MMolecule) -> str:
        filename = molecule.MMolecule.randomString() + '.pdb'
        receptor.write_pdb(filename)
        pymol.cmd.load(filename)
        pymol.cmd.remove('resn HOH')
        pymol.cmd.h_add(selection='acceptors or donors')
        pymol.cmd.save('protein.pdb')
        obabel_input = input.OpenBabelInput(Input=os.path.abspath('protein.pdb'), OutputExt='pdbqt', Args=['-xh'])
        os.remove('protein.pdb')
        os.remove(os.path.abspath(filename))

        return OpenBabel.compute(input_data=obabel_input).Contents

    @classmethod
    def ligand_prep(cls, smiles: str) -> str:

        pdbqt_file = os.path.abspath('tmp.pdbqt')

        with open(pdbqt_file, 'w') as fp:
            fp.write(cls.smi_to_pdbqt(smiles))

        grep_input = input.GrepInput(Input=pdbqt_file, Pattern='ATOM')
        grep_output = Grep.compute(input_data=grep_input)

        os.remove(pdbqt_file)

        return grep_output.Contents

    @classmethod
    def smi_to_pdbqt(cls, smiles: str) -> input.DockingSimInput:

        smi_file = os.path.abspath('tmp.smi')

        with open(smi_file, 'w') as fp:
            fp.write(smiles)

        obabel_input = input.OpenBabelInput(Input=smi_file, OutputExt='pdbqt', Args=['--gen3d', '-h'])
        obabel_output = OpenBabel.compute(input_data=obabel_input)

        os.remove(smi_file)

        return obabel_output.Contents        