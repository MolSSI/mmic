import sys
sys.path.insert(0, '..')

from models import input, molecule
from models import output

from DockingBlueprints.docking_sim_prep_component import DockSimPrepComponent

# Import utility components
from DockingImplementation.grep_component import Grep
from DockingImplementation.openbabel_component import OpenBabel

from typing import Any, Dict, List, Optional, Tuple
import os
import pymol

class AutoDockPrep(DockSimPrepComponent):

    def execute(self, input_data: input.DockingInput, config: "TaskConfig" = None) -> output.DockingPrepOutput:

        binput =  self.build_input(input_data)
        ligand = output.FileOutput(Contents=binput['ligand'])
        receptor = output.FileOutput(Contents=binput['receptor'])

        return True, output.DockingPrepOutput(Ligand=ligand, Receptor=receptor)

    def build_input(self, input_model: input.DockingInput, template: Optional[str] = None) -> Dict[str, Any]:

        ligand = self.ligand_prep(smiles = input_model.Ligand.identifiers.smiles)
        receptor = self.receptor_prep(receptor = input_model.Receptor)

        return {
            "ligand": ligand,
            "receptor": receptor
        }

    # helper functions
    def receptor_prep(self, receptor: molecule.MMolecule) -> str:
        filename = molecule.MMolecule.randomString() + '.pdb'
        receptor.write_pdb(filename)
        pymol.cmd.load(filename)
        pymol.cmd.remove('resn HOH')
        pymol.cmd.h_add(selection='acceptors or donors')

        pdb_name = molecule.MMolecule.randomString() + '.pdb'

        pymol.cmd.save(pdb_name)
        obabel_input = input.OpenBabelInput(Input=os.path.abspath(pdb_name), OutputExt='pdbqt', Args=['-xh'])
        os.remove(pdb_name)
        os.remove(os.path.abspath(filename))

        return OpenBabel.compute(input_data=obabel_input).Contents

    def ligand_prep(self, smiles: str) -> str:

        pdbqt_file = os.path.abspath(molecule.MMolecule.randomString() + '.pdbqt')

        with open(pdbqt_file, 'w') as fp:
            fp.write(self.smi_to_pdbqt(smiles))

        grep_input = input.GrepInput(Input=pdbqt_file, Pattern='ATOM')
        grep_output = Grep.compute(input_data=grep_input)

        os.remove(pdbqt_file)

        return grep_output.Contents

    def smi_to_pdbqt(self, smiles: str) -> str:

        smi_file = os.path.abspath(molecule.MMolecule.randomString() + '.smi')

        with open(smi_file, 'w') as fp:
            fp.write(smiles)

        obabel_input = input.OpenBabelInput(Input=smi_file, OutputExt='pdbqt', Args=['--gen3d', '-h'])
        obabel_output = OpenBabel.compute(input_data=obabel_input)

        os.remove(smi_file)

        return obabel_output.Contents        