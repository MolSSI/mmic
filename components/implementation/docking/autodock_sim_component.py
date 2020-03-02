from typing import Any, Dict, List, Optional, Tuple
from models.components.docking.autodock.input import AutoDockSimInput
from models.components.docking.autodock.output import AutoDockSimOutput
from components.blueprints.utils.cmd_component import CmdComponent
import os

class AutoDockSim(CmdComponent):
    
    @classmethod
    def input(cls):
        return AutoDockSimInput

    @classmethod
    def output(cls):
        return AutoDickSimOutput

    def execute(self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,) -> Tuple[bool, Dict[str, Any]]:


        receptor, ligand = inputs.receptor, inputs.ligand

        with open('receptor.pdbqt', 'w') as fp:
            fp.write(receptor)

        with open('ligand.pdbqt', 'w') as fp:
            fp.write(ligand)

        input_model = inputs.dict()
        input_model['receptor'] = os.path.abspath('receptor.pdbqt')
        input_model['ligand'] = os.path.abspath('ligand.pdbqt')

        input_model['out'] = os.path.abspath('autodock.pdbqt')
        input_model['log'] = os.path.abspath('autodock.log')

        execute_input = self.build_input(input_model)

        exe_success, proc = self.run(execute_input)

        if exe_success:
            return True, self.parse_output(proc, inputs)
        else:
            raise ValueError(proc["stderr"])

    def build_input(
        self, input_model: Dict[str, Any], config: Optional["TaskConfig"] = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        cmd = ["vina"]

        for key, val in input_model.items():
            if val:
                cmd.append('--' + key)
                if isinstance(val, str):
                    cmd.append(val)
                else:
                    cmd.append(str(val))

        print(cmd)
        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": ['system.pdbqt', 'autodock.log'],
            "scratch_directory": scratch_directory,
            "environment": env
        }

    def parse_output(self, outfiles: Dict[str, str], input_model: AutoDockSimInput) -> "CmdOutput":
        
        output_file = outfiles['stdout']

        return CmdOutput(Contents=output_file)