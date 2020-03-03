from typing import List, Optional, Tuple, Union
from qcelemental import models
from models.domains.classmech.molecule import MMolecule
from models.tools.rdkit.codes import ChemCode
from models.components.utils.input import FileInput
from pydantic import Field

class DockingInput(models.ProtoModel):
    ligand: MMolecule = Field(..., description="Molecule model for candidate ligand (e.g. drug).")
    receptor: MMolecule = Field(..., description="Molecule model for receptor (e.g. protein).")
    searchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = Field(None, description="A 3D box defined by (xmin, xmax, ymin, ymax, zmin, zmax)."
        "The search space effectively restricts where the movable atoms, including those in the flexible side chains, should lie.")

class DockingPrepInput(DockingInput):
    ligand: Union[ChemCode, FileInput, MMolecule] = Field(..., description="Molecule model for candidate ligand (e.g. drug).")
    receptor: Union[FileInput, MMolecule] = Field(..., description="Molecule model for receptor (e.g. protein).")

class DockingSimInput(models.ProtoModel):
    dockingInput: DockingInput = Field(..., description="Docking input model.")
    ligand: Union[List[str], List[MMolecule]] = Field(..., description="Molecule model for candidate ligand (e.g. drug).")
    receptor: Union[str, MMolecule] = Field(..., description="Molecule model for receptor (e.g. protein).")