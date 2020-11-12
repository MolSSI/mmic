# What is MMComponents?
The Molecular Mechanics Components (MMComponents) project is a standard for input and output of programs for defining the scientific and computational stages of classical MM pipelines specifying the I/O, but the leaving the implementation up to a developer or user. We define the "what" of the scientific stages without restricting the "how". We define only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment rather than scientist expertise.

<p align="center">
    <img src="mmcomponents/data/imgs/mm_component_hierarchy.png" width="500">
</p>

We construct an abstract Base Component that is inherited by all MMComponent blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.

# Components being developed

## Simulators
- [Autodock vina](https://github.com/MolSSI/MMComponents_autodock): molecular docking engine based on [Autodock Vina](http://vina.scripps.edu)
- [NAMD](https://github.com/MolSSI/MMComponents_namd): molecular dynamics engine based on the [NAMD](https://www.ks.uiuc.edu/Research/namd) simulator

## Builders
- [AutoMartini](https://github.com/MolSSI/MMComponents_automartini): automatic generation of Martini forcefield parameters for small organic molecules

## Translators
- [RDKit](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/rdkit_component.py): RDKit to/from MMSchema converter
- [ParmEd](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/parmed_component.py): ParmEd to/from MMSchema converter
- [MDAnalysis](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/mdanalysis_component.py): MDAnalysis to/from MMSchema converter
