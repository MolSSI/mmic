import sys

sys.path.insert(0, '..')

from models import input
import numpy
import os
from qcelemental import models

natoms = 10
ligand = models.Molecule(geometry=numpy.random.rand(natoms,3) * 10, symbols=['C' for i in range(natoms)])
receptor = models.Molecule(geometry=numpy.random.rand(natoms,3) * 10, symbols=['C' for i in range(natoms)])

docking_input = input.DockingInput(Ligand=ligand, Receptor=receptor)

docking_input_data = input.DockingInputData(
					Ligand='CCC', 
					Receptor='data/PHIPA_C2/PHIPA_C2_apo.pdb'
					)

from DockingImplementation.openbabel_component import OpenBabel
from DockingImplementation.grep_component import Grep
from DockingImplementation.autodock_prep_component import AutoDockPrep
from config import TaskConfig

# Test input file
pdb_file = os.path.abspath('data/PHIPA_C2/PHIPA_C2_apo.pdb')

# Test for openbabel
obabel_input = input.OpenBabelInput(Input=pdb_file, OutputExt='pdbqt')
obabel_output = OpenBabel.compute(input_data=obabel_input)

#with open('test.pdbqt', 'w') as fp:
#	fp.write(obabel_output.FileContents)

# Test for grep
grep_input = input.GrepInput(Input=pdb_file, Pattern='REMARK')
grep_output = Grep.compute(input_data=grep_input)

#with open('test.grep', 'w') as fp:
#	fp.write(grep_output.FileContents)

# Test for AutodockPrep
ADP = AutoDockPrep.compute(input_data=docking_input_data)

print(ADP.keys())
