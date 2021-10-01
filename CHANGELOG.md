# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2021-07-19

- Initial release of mmic

## [0.1.1] - 2021-10-01
- ([`:pr:2`](https://github.com/MolSSI/mmic/pull/2)) Converts `get_version` to classmethod in all blueprint components. Converts `installed_comps` and `tactic_comps` to classproperty in `StrategyComponent`.
- ([`:pr:3`](https://github.com/MolSSI/mmic/pull/3)) Replaces classmethod `get_verion` with classproperty `version` in all components. Removes abc methods from blueprint components. Changes input/output abstract classmethods to classproperties. Adds test routine for ProgramHarness.
