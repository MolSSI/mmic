from typing import Any, Dict, List, Optional, Tuple
from models.components.docking.autodock.input import AutoDockSimInput
from models.components.docking.autodock.output import AutoDockSimOutput
from models.components.utils.output import CmdOutput
from models.components.utils.input import FileInput
from components.blueprints.utils.cmd_component import CmdComponent
import os

class AutoDockSimComponent(CmdComponent):
    
    @classmethod
    def input(cls):
        return AutoDockSimInput

    @classmethod
    def output(cls):
        return AutoDockSimOutput

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
        del input_model['dockingInput']

        input_model['receptor'] = os.path.abspath('receptor.pdbqt')
        input_model['ligand'] = os.path.abspath('ligand.pdbqt')

        execute_input = self.build_input(input_model)

        exe_success, proc = self.run(execute_input)

        if exe_success:
            output = True, self.parse_output(proc, inputs)
            self.cleanup()
            return output
        else:
            self.cleanup()
            raise ValueError(proc["stderr"])

    def cleanup(self):
        for file in ['receptor.pdbqt', 'ligand.pdbqt', 'autodock.pdbqt', 'autodock.log']:
            if os.path.isfile(file):
                os.remove(file)

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

        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": [os.path.abspath('autodock.pdbqt'), os.path.abspath('autodock.log')],
            "scratch_directory": scratch_directory,
            "environment": env
        }

    def parse_output(self, output: Dict[str, str], input_model: AutoDockSimInput) -> AutoDockSimOutput:
        stdout = output['stdout']
        stderr = output['stderr']
        outfiles = output['outfiles']

        if stderr:
            print("Error from AutoDock Vina:")
            print("=========================")
            print(stderr)

        system, log = outfiles
        cmdout = CmdOutput(stdout=stdout, stderr=stderr, log=FileInput(path=log).read())

        return AutoDockSimOutput(
                    cmdout=cmdout, 
                    system=FileInput(path=system).read(),
                    dockingInput=input_model.dockingInput
                )