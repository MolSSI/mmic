"""
TaskConfig Model
"""
from typing import Optional
import pydantic


class TaskConfig(pydantic.BaseModel):
    """Description of the configuration used to launch a task."""

    # Specifications
    ncores: int = pydantic.Field(None, description="Number cores per task on each node")
    nnodes: int  # Number of nodes per task
    memory: float  # Amount of memory in GiB per node
    scratch_directory: Optional[str]  # What location to use as scratch
    retries: int  # Number of retries on random failures
    mpiexec_command: Optional[
        str
    ]  # Command used to launch MPI tasks, see NodeDescriptor
    use_mpiexec: bool = False  # Whether it is necessary to use MPI to run an executable
    cores_per_rank: int = pydantic.Field(1, description="Number of cores per MPI rank")

    class Config:
        extra = "forbid"
