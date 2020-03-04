from typing import List, Optional, Union
from qcelemental import models
from pydantic import validator
import os

from .output import FileOutput
from pathlib import Path

class FileInput(models.ProtoModel):
    path: str

    @validator('path')
    def _exists(cls, v):
        if not os.path.isfile(v):
            raise IOError(f'Input file {v} does not eixst.')

        return v

    @property
    def ext(self):
        return Path(self.path).suffix

    def read(self) -> str:
        with open(self.path, 'r') as fp:
            return fp.read()

class CmdInput(models.ProtoModel):
    fileInput: Union[FileInput, List[FileInput]]
    fileOutput: Optional[Union[FileOutput, List[FileOutput]]] = None
    args: Optional[List[str]] = None

class OpenBabelInput(CmdInput):
    outputExt: str
    
class GrepInput(CmdInput):
    pattern: str