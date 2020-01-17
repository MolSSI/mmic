import sys
sys.path.insert(0, '..')

from qcengine.util import temporary_directory, execute
from base_component.base_component import ProgramHarness
from DockingApps.openbabel_component import OpenBabel

from typing import Any, Dict, List, Optional, Tuple
import os
import pymol



class AutoDockPrep(ProgramHarness):

    @classmethod
    def compute(cls, input_data: Dict[str, str]) -> str:
        filename = input_data['filename']

        execute_input = cls.build_input(filename)
        exe_success, proc = cls.execute(execute_input)

        cls.cleanup(['temp.pdbqt', 'protein.pdb'])
        cls.parse_output(proc['stdout'], 'receptor.pdbqt')

    @classmethod
    def build_input(
        cls, filename: str, template: Optional[str] = None
    ) -> Dict[str, Any]:
        
        pymol.cmd.load(filename)
        pymol.cmd.remove('resn HOH')
        pymol.cmd.h_add(selection='acceptors or donors')
        pymol.cmd.save('protein.pdb')
        OpenBabel.compute(input_data={'input':os.path.abspath('protein.pdb'), 'output':'temp.pdbqt', 'args':'-xh'})

        return {
            "command": ['grep', 'ATOM', os.path.abspath('temp.pdbqt')],
            "infiles": None,
            "outfiles": None,
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
    def cleanup(cls, files: List[str]):
        for file in files:
            os.remove(file)

    @classmethod
    def parse_output(cls, outfile: str, filename: str) -> Any:

        with open(filename, 'w') as fp:
            fp.write(outfile)