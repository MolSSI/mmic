import input
import numpy
from qcelemental import models

natoms = 10
ligand = models.Molecule(geometry=numpy.random.rand(natoms,3) * 10, symbols=['C' for i in range(natoms)])
receptor = models.Molecule(geometry=numpy.random.rand(natoms,3) * 10, symbols=['C' for i in range(natoms)])

docking_input = input.DockingInput(Ligand=ligand, Receptor=receptor)

docking_input_data = input.DockingInputData(
					LigandPath='../data/PHIPA_C2/fragments_screened.csv', 
					ReceptorPath='../data/PHIPA_C2/PHIPA_C2_apo.pdb'z
					)
