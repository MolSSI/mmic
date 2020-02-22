from typing import List, Optional, Union
from qcelemental import models

class CmdInput(models.ProtoModel):
    Input: Union[str, List[str]]
    Output: Optional[str] = None
    Args: Optional[List[str]] = None

class OpenBabelInput(CmdInput):
    OutputExt: str
    
class GrepInput(CmdInput):
    Pattern: str