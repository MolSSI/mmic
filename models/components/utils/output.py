from qcelemental import models
from typing import List, Optional, Union
from pydantic import validator
from pathlib import Path

class CmdOutput(models.ProtoModel):
    Contents: str

class FileOutput(models.ProtoModel):
    path: str

    @validator('path')
    def _exists(cls, v):
        if os.path.isfile(v):
            raise IOError(f'File {v} already eixsts.')
        return v

    @property
    def ext(self):
        return Path(self.path).suffix