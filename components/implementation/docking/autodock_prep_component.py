from models.components.docking.autodock.input import AutoDockSimInput
from models.components.docking.input import DockingInput
from models.components.utils.input import OpenBabelInput, FileInput
from models.components.utils.output import FileOutput
from models.molecmech.molecules.mm_molecule import MMolecule

from components.blueprints.docking.docking_prep_component import DockPrepComponent
from components.implementation.utils.openbabel_component import OpenBabel

from typing import Any, Dict, List, Optional, Tuple
import os

class AutoDockPrepComponent(DockPrepComponent):

    @classmethod
    def output(cls):
        return AutoDockSimInput

    def execute(self, input_data: DockingInput, config: "TaskConfig" = None) -> Tuple[bool, AutoDockSimInput]:
        binput = self.build_input(input_data)
        return True, AutoDockSimInput(dockingInput=input_data, **binput)

    def build_input(self, input_model: DockingInput, template: Optional[str] = None) -> Dict[str, Any]:
        ligand_pdbqt = self.ligand_prep(smiles = input_model.ligand.identifiers.smiles)
        receptor_pdbqt = self.receptor_prep(receptor = input_model.receptor)
        inputDict = self.checkSimParams(input_model)
        inputDict['ligand'] = ligand_pdbqt
        inputDict['receptor'] = receptor_pdbqt

        return inputDict

    # helper functions
    def receptor_prep(self, receptor: MMolecule) -> str:
        pdb_name = DockPrepComponent.randomString() + '.pdb'
        fo = FileOutput(path=os.path.abspath(pdb_name))
        receptor.to_file(fo.path)

        # Assume protein is rigid and ass missing hydrogens
        obabel_input = OpenBabelInput(fileInput=FileInput(path=fo.path), outputExt='pdbqt', args=['-xrh'])
        final_receptor = OpenBabel.compute(input_data=obabel_input).stdout
        fo.remove()

        return final_receptor

    def ligand_prep(self, smiles: "ChemCode") -> str:
        return self.smi_to_pdbqt(smiles.code)

    def smi_to_pdbqt(self, smiles: str) -> str:
        smi_file = os.path.abspath(DockPrepComponent.randomString() + '.smi')

        with open(smi_file, 'w') as fp:
            fp.write(smiles)

        obabel_input = OpenBabelInput(fileInput=FileInput(path=smi_file), outputExt='pdbqt', args=['--gen3d', '-h'])
        obabel_output = OpenBabel.compute(input_data=obabel_input)

        os.remove(smi_file)

        return obabel_output.stdout        

    def checkSimParams(self, input_model: DockingInput) -> Dict[str, Any]:
        receptor = input_model.receptor
        outputDict = {}
        inputDict = input_model.dict()

        if not (inputDict.get('center_x') and inputDict.get('size_x')):
            xmin, xmax = receptor.geometry[:,0].min(), receptor.geometry[:,0].max()
            outputDict['center_x'] = (xmin + xmax) / 2.0
            outputDict['size_x'] = xmax - xmin

        if not (inputDict.get('center_y') and inputDict.get('size_y')):
            ymin, ymax = receptor.geometry[:,1].min(), receptor.geometry[:,1].max()
            outputDict['center_y'] = (ymin + ymax) / 2.0
            outputDict['size_y'] = ymax - ymin

        if not (inputDict.get('center_z') and inputDict.get('size_z')):
            zmin, zmax = receptor.geometry[:,2].min(), receptor.geometry[:,2].max()
            outputDict['center_z'] = (zmin + zmax) / 2.0
            outputDict['size_z'] = zmax - zmin

        outputDict['out'] = os.path.abspath('autodock.pdbqt')
        outputDict['log'] = os.path.abspath('autodock.log')

        return outputDict
