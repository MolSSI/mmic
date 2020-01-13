import input
import numpy
from qcelemental import models

natoms = 10
ligand = models.Molecule(geometry=numpy.random.rand(natoms,3) * 10, symbols=['C' for i in range(natoms)])
receptor = models.Molecule(geometry=numpy.random.rand(natoms,3) * 10, symbols=['C' for i in range(natoms)])

docking_input = input.Docking(Ligand=ligand, Receptor=receptor)
