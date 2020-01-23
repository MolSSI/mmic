import sys
sys.path.insert(0, '..')

from qcengine.util import temporary_directory, execute
from qcelemental import models
from base_component.base_component import ProgramHarness
from typing import Any, Dict, List, Optional, Tuple
import os
from models.input import CmdInput
from models.output import CmdOutput

class Grep(ProgramHarness):

    _defaults = {
        "name": "Grep",
        "scratch": False,
        "thread_safe": True,
        "thread_parallel": False,
        "node_parallel": False,
        "managed_memory": True,
    }

    @classmethod
    def compute(cls, input_data: CmdInput, config: Optional["TaskConfig"] = None) -> CmdOutput:

        args = input_data.Args

        input_model = {'input': input_data.Input, 'pattern': input_data.Pattern, 'args': args}

        execute_input = cls.build_input(input_model, config)
        exe_success, proc = cls.execute(execute_input)

        if exe_success:
            return cls.parse_output(proc, input_model)
        else:
            raise ValueError(proc["stderr"])

    @classmethod
    def build_input(
        cls, input_model: Dict[str, Any], config: Optional["TaskConfig"] = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        cmd = ["grep"]

        if input_model['args']:
            for arg in input_model['args']:
                cmd.append(arg)

        cmd.append(input_model['pattern']) 

        if isinstance(input_model['input'], list):
            for ginput in input_model['input']:
                cmd.append(ginput)
        elif isinstance(input_model['input'], str):
            cmd.append(input_model['input'])
        else:
            raise Exception

        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": None,
            "scratch_directory": scratch_directory,
            "environment": env
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
    def parse_output(cls, outfiles: Dict[str, str], input_model: Dict[str, Any]) -> CmdOutput:
        
        output_file = outfiles['stdout']

        return CmdOutput(FileContents=output_file)
