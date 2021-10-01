[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic/context:python)

# What is MMIC?
The Molecular Mechanics Interoperable Components (MMIC) project provides a standard for input and output of MM programs by defining the scientific and computational stages of classical MM pipelines, but leaving the implementation up to the developer/user. MMIC attempts to define the "what" of scientific stages without restricting the "how" i.e. MMIC defines only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment without the need for deep scientific expertise.

<p align="center">
    <img src="mmic/data/imgs/mm_component_hierarchy.png" width="500">
</p>

We construct an abstract Base Component that is inherited by all MMComponent blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.

# Components being developed

See the [MM portal](https://mm-portal.netlify.app/components) for the latest updates.
