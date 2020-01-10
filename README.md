
 # Problem
 Given the 3D structures of 2 (or more) molecules, we need to determine the optimal binding modes. This requires computing a "score" function corresponding to each "pose" or 3D conformation of the complex. This is commonly referred to as a "docking" simulation. If molecular docking is applied to a series of ligand molecules, then this is referred to as "virtual screening". Virtual screening is frequently employed in structure-based drug design because it enables the identification of a drug that binds optimally to a specific target molecule such as a protein.

<img src="https://www.oist.jp/sites/default/files/photos/docking%20simulation.png" width="500">

Applications of docking include:

- Virtual screening (hit identification)
- Drug discovery (lead optimization)
- Binding site identification (blind docking)
- Protein-protein interactions
- Enzymatic reaction mechanisms
- Protein engineering


<img src="docking-soft.png" width="500">


# MVPs

## Components

### Component 1:
    Take fragalysis file as input
    Provide DockingModel Output

### Component 2:
    Take DockingModel input
    Provide DockingResult output

### Component3:
    Take DockingModel and DockingResult input
    Provide affinity (float)

## Models
### DockingModel:
    Ligand(Molecule)
    Protein/Target(Molecule)
    
### DockingOutput:
    Poses(List[Molecule])
    Scores(List[float])

# Schema

## System definition -> MMSchema
```
System = {
  'box': definition of a simulation box,
  'molecule': [receptor1, ... ligand1, ligand2, ..., ions] 
  'solvent':
   {
      'implicit':
          [
              {
               'model': gen-born,
               'dielectric': 80,
               'salinity': 0.1,
               ...
              }
          ]
      'explicit': [molecule1, molecule2, ...]
    }
}

Molecule = {
  'smiles/pdbID/... (None)': 'some_code',
  'concentration (None)': float,
  'positions (None)': [x,y,z],
  'bonds (None)': [[index1, index2], ...],
  'bond_order (None)': [bo1, bo2, ...],
  'forcefield': ['amber99', 'charmm36', ...]
}
```

## System preparation
```
Refinement = {
  'hydrogens (None)': True/False,
  'add_residues (False)': True/False,
  'extract (None)': group_name,
  'isomers (False)': True/False
}

Minimization = {
   'MMparams': ...
}
```
## Simulation 
```
Simulation = {
  'target': receptor1,
  'ligand': [ligand1, ligand2, ...],
  'search_region (None)': [[region1_ligand1, region2_ligand1, ...], [region1_ligand2, ...], ...],
  'interaction': 'all-atom i.e. pairwise', 'coarse-grained e.g. grid', ...,
  'rigid': [receptor1, ligand1, ...],
  'seed': long int, 
  'MCparams': ...,
  'MMparams': ...
}
```

# Questions
- Support CG/MD?
- Support covalent bonding (b/w ligand and receptor)?
- User-supplied conformers?
- Support for empirical and knowledge-based methods (in contrast to FFs)?
- How many docking software to support? There's over 50 ...
- Which FFs should we support?
