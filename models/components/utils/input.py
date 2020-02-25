from typing import List, Optional, Union
from qcelemental import models
from pydantic import validator
import os

from .output import FileOutput

class FileInput(models.ProtoModel):
    path: str

    @validator('path')
    def exists(cls, v):
        if not os.path.isfile(v):
            raise IOError(f'Input file {v} does not eixst.')

        return v

class CmdInput(models.ProtoModel):
    fileInput: Union[FileInput, List[FileInput]]
    fileOutput: Optional[Union[FileOutput, List[FileOutput]]] = None
    args: Optional[List[str]] = None

class OpenBabelInput(CmdInput):
    outputExt: str
    
class GrepInput(CmdInput):
    pattern: str