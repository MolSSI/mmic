
 # Problem
 Given the 3D structures of 2 (or more) molecules, we need to determine the optimal binding modes. This requires computing a "score" function corresponding to each "pose" or conformation between the 2 molecules. This is commonly referred to as a "docking" simulation. If docking is applied to a series of ligand molecules this is referred to as "virtual screening". Molecular docking with virtual screening is frequently employed in structure-based drug design because it enables the identification of drugs that bind optimally to a specific target molecule such as a protein.

<img src="https://www.oist.jp/sites/default/files/photos/docking%20simulation.png" width="500">


# Schema

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
  'smiles (None)': 'some_code',
  'pdbID (None)': 'some_code',
  'concentration (None)': float,
  'positions (None)': [x,y,z],
  'topology (None)': [connectivity, ...],
  'forcefield': ['amber99', 'charmm36', ...]
}

Simulation = {
  'target': receptor1,
  'ligand': [ligand1, ligand2, ...],
  'search_region (None)': [[region1_ligand1, region2_ligand1, ...], [region1_ligand2, ...], ...],
  'interaction': 'all-atom i.e. pairwise', 'coarse-grained e.g. grid', ...,
  'seed': long int 
}
```

# Questions
- Is CG/MD supported?
- Is covalent bonding (b/w ligand and receptor) supported?
