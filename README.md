# What is MMComponents?
The Molecular Mechanics Components (MMComponents) project is a standard for input and output of programs for defining the scientific and computational stages of classical MM pipelines specifying the I/O, but the leaving the implementation up to a developer or user. We define the "what" of the scientific stages without restricting the "how". We define only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment rather than scientist expertise.

<p align="center">
    <img src="data/imgs/mm_component_hierarchy.png" width="500">
</p>

We construct an abstract Base Component that is inherited by all MMComponent blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.
 
# MMComponent Example: Molecular Docking
## What is Docking?
Docking is a computational technique used to determine the optimal binding modes of a ligand-receptor system. A ligand is typically a small (e.g. drug) molecule that binds to a macromolecular receptor such as a protein. A docking simulation estimates the strength of the binding (or a quantitative "score") in the vicinity of the receptor's binding site. Each score corresponds to the 3D conformation and orientation (or "pose") of the ligand relative to the receptor.

<p align="center">
<img src="data/imgs/docking-sys.png" width="500">
</p>
    
Applications of docking include:

- Virtual screening (hit identification)
- Drug discovery (lead optimization)
- Binding site identification (blind docking)
- Protein-protein interactions
- Enzymatic reaction mechanisms
- Protein engineering

## Docking Component
### Preparing Input

<p align="center">
<img src="data/imgs/autodock.png">
</p>

```python
# Import converter component for autodock vina
from components.implementation.docking.autodock_convert_component import ConvertAutoDockComponent

# Import docking data model
from models.components.docking.input import DockingRawInput

# Construct docking input
receptor = 'data/dialanine/dialanine.pdb'
ligand = 'CCC' # smiles code for propane
dockRawInput = DockingRawInput(ligand=ligand, receptor=receptor)
dockInput = ConvertAutoDockComponent.compute(dockRawInput)
```

### Running Docking with AutoDock Vina
```python
# Import docking simulation component for autodock vina
from components.implementation.docking.autodock_component import AutoDockComponent

# Run autodock vina
dockOutput = AutoDockComponent.compute(dockInput)

# Extract output
scores, poses = dockOutput.scores, dockOutput.poses
```
