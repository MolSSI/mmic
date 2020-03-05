from components.blueprints.utils.cmd_component import CmdComponent
from typing import Any, Dict, List, Optional, Tuple
import os
from models.components.utils.input import OpenBabelInput
from models.components.utils.output import CmdOutput

class OpenBabel(CmdComponent):

    @classmethod
    def input(cls):
        return OpenBabelInput

    @classmethod
    def output(cls):
        return CmdOutput

    def build_input(
        self, input_model: OpenBabelInput, config: "TaskConfig" = None, template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        output = 'tmp.' + input_model.outputExt
        cmd = ["obabel", input_model.fileInput.path, "-O" + output]

        if input_model.args:
            for arg in input_model.args:
                cmd.append(arg)

        env = os.environ.copy()

        if config:
            env["MKL_NUM_THREADS"] = str(config.ncores)
            env["OMP_NUM_THREADS"] = str(config.ncores)

        scratch_directory = config.scratch_directory if config else None

        return {
            "command": cmd,
            "infiles": None,
            "outfiles": [output],
            "scratch_directory": scratch_directory,
            "environment": env
        }

    def parse_output(self, outfiles: Dict[str, Dict[str, str]], input_model: OpenBabelInput) -> CmdOutput:
        
        output_file = outfiles['outfiles']['tmp.' + input_model.outputExt]

        return CmdOutput(stdout=output_file)
