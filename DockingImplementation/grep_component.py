import sys
sys.path.insert(0, '..')

from qcengine.util import temporary_directory, execute
from qcelemental import models
from base_component.base_component import ProgramHarness
from typing import Any, Dict, List, Optional, Tuple
import os
from models.input import GrepInput
from models.output import FileOutput

class Grep(ProgramHarness):

    @classmethod
    def input(cls):
        return GrepInput

    @classmethod
    def output(cls):
        return FileOutput

    def execute(self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,) -> Tuple[bool, Dict[str, Any]]:

        args = inputs.Args

        input_model = {'input': inputs.Input, 'pattern': inputs.Pattern, 'args': args}

        execute_input = self.build_input(input_model)

        exe_success, proc = self.run(execute_input)

        if exe_success:
            return True, self.parse_output(proc, input_model)
        else:
            raise ValueError(proc["stderr"])

    def build_input(
        self, input_model: Dict[str, Any], config: Optional["TaskConfig"] = None, template: Optional[str] = None
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

    def found(raise_error: bool = False) -> bool:
        """
        Checks if the program can be found.
        Parameters
        ----------
        raise_error : bool, optional
            If True, raises an error if the program cannot be found.
        Returns
        -------
        bool
            Returns True if the program was found, False otherwise.
        """

    def parse_output(self, outfiles: Dict[str, str], input_model: Dict[str, Any]) -> FileOutput:
        
        output_file = outfiles['stdout']

        return FileOutput(Contents=output_file)

    def run(
        self,
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