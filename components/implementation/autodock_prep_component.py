import sys
sys.path.insert(0, '..')

from models.components.docking.autodock.input import AutoDockSimInput
from models.components.docking.input import DockingInput
from models.components.utils.input import OpenBabelInput
import models.domains.docking.molecule as molecule

from components.blueprints.docking_sim_prep_component import DockSimPrepComponent

# Import utility components
from components.implementation.grep_component import Grep
from components.implementation.openbabel_component import OpenBabel

from typing import Any, Dict, List, Optional, Tuple
import os
import pymol

class AutoDockPrep(DockSimPrepComponent):

    def execute(self, input_data: DockingInput, config: "TaskConfig" = None) -> AutoDockSimInput:
        
        binput = self.build_input(input_data)
        return True, AutoDockSimInput(Ligand=binput['ligand_pdbqt'], Receptor=binput['receptor_pdbqt'])


    def build_input(self, input_model: DockingInput, template: Optional[str] = None) -> Dict[str, Any]:

        ligand_pdbqt = self.ligand_prep(smiles = input_model.Ligand.identifiers.smiles)
        receptor_pdbqt = self.receptor_prep(receptor = input_model.Receptor)

        return {'ligand_pdbqt': ligand_pdbqt, 'receptor_pdbqt': receptor_pdbqt}

    # helper functions
    def receptor_prep(self, receptor: molecule.MMolecule) -> str:
        
        pymol.cmd.remove('resn HOH')
        pymol.cmd.h_add(selection='acceptors or donors')

        pdb_name = molecule.MMolecule.randomString() + '.pdb'

        pymol.cmd.save(pdb_name)

        # Assume protein is rigid and ass missing hydrogens
        obabel_input = OpenBabelInput(Input=os.path.abspath(pdb_name), OutputExt='pdbqt', Args=['-xrh'])
        final_receptor = OpenBabel.compute(input_data=obabel_input).Contents

        os.remove(pdb_name)
        receptor.clear_pdb()

        return final_receptor

    def ligand_prep(self, smiles: str) -> str:

        return self.smi_to_pdbqt(smiles)

    def smi_to_pdbqt(self, smiles: str) -> str:

        smi_file = os.path.abspath(molecule.MMolecule.randomString() + '.smi')

        with open(smi_file, 'w') as fp:
            fp.write(smiles)

        obabel_input = OpenBabelInput(Input=smi_file, OutputExt='pdbqt', Args=['--gen3d', '-h'])
        obabel_output = OpenBabel.compute(input_data=obabel_input)

        os.remove(smi_file)

        return obabel_output.Contents        