from mmcomponents.models.components.docking.autodock.output import AutoDockSimOutput
from mmcomponents.models.components.docking.output import DockingOutput
from mmelemental.models.components.utils.input import OpenBabelInput, FileInput
from mmelemental.models.components.utils.output import FileOutput
from mmelemental.models.molecmech.molecules.mm_molecule import Molecule
from mmelemental.models.components.utils.output import CmdOutput 

from mmcomponents.components.blueprints.docking.docking_post_component import DockPostComponent
from mmcomponents.components.implementation.utils.openbabel_component import OpenBabel
from mmcomponents.components.blueprints.utils.cmd_component import CmdComponent

from typing import Any, Dict, List, Optional, Tuple
import os

class AutoDockPostComponent(DockPostComponent, CmdComponent):
    """ Postprocessing autodock component. """

    @classmethod
    def input(cls):
        return AutoDockSimOutput

    def build_input(self, input_model: AutoDockSimOutput, config: "TaskConfig" = None, 
        template: Optional[str] = None) -> Dict[str, Any]:
        """ Builds input files for autodock vina_split. """

        cmdout, system = input_model.cmdout, input_model.system
        _, scores = self.parse_scores(cmdout)

        fsystem = FileOutput(path=os.path.abspath('system.pdbqt'))
        fsystem.write(system)

        cmd = ["vina_split", '--input', fsystem.path, '--ligand', 'ligand', '--flex', 'flex']
        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": ['ligand*', 'flex*'],
            "scratch_directory": scratch_directory,
            "environment": env,
            "clean_files": fsystem
        }

    def parse_output(self, outfiles: Dict[str, Dict[str, str]], input_model: AutoDockSimOutput) -> DockingOutput:
        """ Parses output from vina_split. """

        ligands = outfiles['outfiles']['ligand*']
        poses = []

        for ligname in ligands:
            pdbqt = FileOutput(path=os.path.abspath(ligname))
            pdbqt.write(ligands[ligname])
            
            obabel_input = OpenBabelInput(fileInput=FileInput(path=pdbqt.path), outputExt='pdb')
            
            ligand_pdb = OpenBabel.compute(input_data=obabel_input).stdout
            pdb = FileOutput(path=os.path.abspath('ligand.pdb'))
            pdb.write(ligand_pdb)

            poses.append(Molecule.from_file(pdb.path))
            pdbqt.remove()
            pdb.remove()

        cmdout = input_model.cmdout
        _, scores = self.parse_scores(cmdout)

        return DockingOutput(dockingInput=input_model.dockingInput, poses=poses, scores=scores)

    # Helper methods
    def parse_scores(self, cmdout: CmdOutput) -> Tuple[List[int], List[float]]:
        """ 
        Extracts scores from autodock vina command-line output. 
        .. todo:: Extract and return RMSD values. 
        """
        read_scores = False
        scores, trials = [], []

        for line in cmdout.stdout.split('\n'):
            if line == '-----+------------+----------+----------':
                read_scores = True
                continue
            elif 'Writing output' in line:
                break
            if read_scores:
                trial, score, _, _ = line.split()
                trials.append(int(trial))
                scores.append(float(score))

        return trials, scores
