import sys
sys.path.insert(0, '..')

from DockingBlueprints.cmd_component import CmdComponent
from typing import Any, Dict, List, Optional, Tuple
import os
from models.input import OpenBabelInput
from models.output import FileOutput

class OpenBabel(CmdComponent):

    @classmethod
    def input(cls):
        return OpenBabelInput

    @classmethod
    def output(cls):
        return FileOutput

    def execute(self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,) -> Tuple[bool, Dict[str, Any]]:

        inp = inputs.Input
        inp_ext = inp.split('.')[-1]

        outp_ext = inputs.OutputExt

        args = inputs.Args

        input_model = {'input': inp, 'input_ext': inp_ext, 'output': 'tmp.' + outp_ext, 'output_ext': outp_ext, 'args': args}

        execute_input = self.build_input(input_model)
        exe_success, proc = self.run(execute_input)

        if exe_success:
            return True, self.parse_output(proc['outfiles'], input_model)
        else:
            raise ValueError(proc["stderr"]) 

    def build_input(
        self, input_model: Dict[str, Any], config: "TaskConfig" = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        cmd = ["obabel", "-i{}".format(input_model['input_ext']), input_model['input'], \
                        "-o{}".format(input_model['output_ext']), "-O{}".format(input_model['output'])]

        if input_model['args']:
            for arg in input_model['args']:
                cmd.append(arg)

        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": [input_model['output']],
            "scratch_directory": scratch_directory,
            "environment": env
        }

    def parse_output(self, outfiles: Dict[str, str], input_model: Dict[str, Any]) -> FileOutput:
        
        output_file = outfiles[input_model['output']]

        return FileOutput(Contents=output_file)
