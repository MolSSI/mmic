import sys
sys.path.insert(0, '..')

from qcengine.util import temporary_directory, execute
from .base_component import ProgramHarness
from typing import Any, Dict, List, Optional, Tuple
import os

class OpenBabel(ProgramHarness):

    @classmethod
    def compute(cls, input_data: Dict[str, str]) -> str:
        inp = input_data['input']
        inp_ext = inp.split('.')[-1]

        outp = input_data['output']
        outp_ext = outp.split('.')[-1]

        args = input_data.get('args')

        input_model = {'input': inp, 'input_ext': inp_ext, 'output': outp, 'output_ext': outp_ext, 'args': args}

        execute_input = cls.build_input(input_model)
        exe_success, proc = cls.execute(execute_input)
        cls.parse_output(proc['outfiles'], input_model)

    @classmethod
    def build_input(
        cls, input_model: Dict[str, Any], template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        cmd = ["obabel", "-i{}".format(input_model['input_ext']), input_model['input'], \
                        "-o{}".format(input_model['output_ext']), "-O{}".format(input_model['output'])]

        if input_model['args']:
            cmd.append(input_model['args'])

        return {
            "command": cmd,
            "infiles": {"-i": input_model['input_ext']},
            "outfiles": [input_model['output']],
            "scratch_directory": None,
            "environment": os.environ.copy()
        }

    @classmethod
    def execute(
        cls,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        infiles = inputs["infiles"]

        outfiles = inputs["outfiles"]
        if extra_outfiles is not None:
            outfiles.extend(extra_outfiles)

        command = inputs["command"]
        if extra_commands is not None:
            command.extend(extra_commands)

        exe_success, proc = execute(
            command,
            infiles=infiles,
            outfiles=outfiles,
            scratch_directory=inputs["scratch_directory"],
            scratch_name=scratch_name,
            timeout=timeout,
            environment=inputs.get("environment", None),
        )
        return exe_success, proc

    @classmethod
    def parse_output(cls, outfiles: Dict[str, str], input_model: Dict[str, Any]) -> Any:
        
        output_file = outfiles[input_model['output']]

        with open(input_model['output'], 'w') as fp:
            fp.write(output_file)
