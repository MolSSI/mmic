from qcengine.util import execute
from qcelemental import models
from mmelemental.models.util.output import FileOutput
from mmcomponents.components.base.base_component import ProgramHarness
from typing import Any, Dict, List, Optional, Tuple, Union

class CmdComponent(ProgramHarness):

    @classmethod
    def input(cls):
        return models.ProtoModel

    @classmethod
    def output(cls):
        return models.ProtoModel

    def clean(self, files: Union[List[FileOutput], FileOutput]):
        if isinstance(files, list):
            for file in files:
                file.remove()
        else:
            files.remove()

    def execute(self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None
    ) -> Tuple[bool, Dict[str, Any]]:

        execute_input = self.build_input(inputs)
        exe_success, proc = self.run(execute_input, clean_files=execute_input.get('clean_files'))

        if exe_success:
            return True, self.parse_output(proc, inputs)
        else:
            raise ValueError(proc["stderr"])

    def run(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
        clean_files: Optional[Union[List[FileOutput], FileOutput]] = None
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
            environment=inputs.get("environment", None)
        )

        if clean_files:
            self.clean(clean_files)
        
        return exe_success, proc