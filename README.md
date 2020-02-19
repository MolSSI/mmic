
 # Problem
 Given the 3D structures of 2 (or more) molecules, we need to determine the optimal binding modes. This requires computing a "score" function corresponding to each "pose" or 3D conformation of the complex. This is commonly referred to as a "docking" simulation. If molecular docking is applied to a series of ligand molecules, then this is referred to as "virtual screening". Virtual screening is frequently employed in structure-based drug design because it enables the identification of a drug that binds optimally to a specific target molecule such as a protein.

<img src="imgs/docking-sys.png" width="500">

Applications of docking include:

- Virtual screening (hit identification)
- Drug discovery (lead optimization)
- Binding site identification (blind docking)
- Protein-protein interactions
- Enzymatic reaction mechanisms
- Protein engineering

# Example: AutoDock Component

<img src="imgs/autodock.png" width="900">

```python
from MMComponents.models.input import DockingInput

dockingIn = DockingInput(Ligand, Receptor)

from MMComponents.implementation.autodock_component import AutoDockComponent

dockingOut = AutoDockComponent.compute(dockingIn)

scores, poses = dockingOut.scores, dockingOut.poses
```
