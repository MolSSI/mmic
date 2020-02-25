from typing import List, Optional, Union
from qcelemental import models
from pydantic import validator
import os

class ChemCode(models.ProtoModel):
    code: str

    @validator('code')
    def validCode(cls, v):
        return v