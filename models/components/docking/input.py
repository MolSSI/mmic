from typing import List, Optional, Tuple, Union
from qcelemental import models
from models.molecmech.molecules.mm_molecule import MMolecule
from models.molecmech.chem.codes import ChemCode
from models.components.utils.input import FileInput
from pydantic import Field

class DockingInput(models.ProtoModel):
    ligand: MMolecule = Field(
        ..., 
        description = "Molecule model for candidate ligand (e.g. drug)."
    )
    receptor: MMolecule = Field(
        ..., 
        description = "Molecule model for receptor (e.g. protein)."
    )
    searchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = Field(
        None, 
        description = "A 3D box defined by (xmin, xmax, ymin, ymax, zmin, zmax)."
        "The search space effectively restricts where the movable atoms, including those in the flexible side chains, should lie."
    )

class DockingPrepInput(DockingInput):
    ligand: Union[ChemCode, FileInput, MMolecule] = Field(
        ..., 
        description = "Molecule model for candidate ligand (e.g. drug)."
    )
    receptor: Union[FileInput, MMolecule] = Field(
        ..., 
        description = "Molecule model for receptor (e.g. protein)."
    )

class DockingSimInput(models.ProtoModel):
    dockingInput: DockingInput = Field(
        ..., 
        description = "Docking input model."
    )
    ligand: str = Field(
        ..., 
        description = "Ligand file string."
    )
    receptor: str = Field(
        ..., 
        description = "Receptor file string."
    )
    cpu: Optional[int] = Field(
        1, 
        description = "The number of CPUs to use. The default is to try to "
        "detect the number of CPUs."
    )
    out: Optional[str] = Field(
        None, 
        description = "Output models."
    )
    log: Optional[str] = Field(
        None, 
        description = "Log file output."
    )
