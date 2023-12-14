# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog], and the project adheres to
[Semantic Versioning].

[Keep a Changelog]:
https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]:
https://semver.org/spec/v2.0.0.html


## [Unreleased]

### Added
- Support for Python 3.12.

### Fixed
- Fix `pylegacy.datetime` tests when running on Windows.

## [0.2.0] - 2023-10-21

### Added
- Backport support for the following features:
  - 2.6 <= Python < 3.3: `shutil.which`.

### Changed
- Upgrade lint dependencies:
  - Update upper limit for `flake8` to 6.2.
  - Restrict `pylint` dependency limits for Python 3.6.

## [0.1.1] - 2023-01-24

### Changed
- Update upper pin for `flake8` to 5.1 in lint requirements.

### Fixed
- Fix setup metadata to allow support for Python 3.11.

## [0.1.0] - 2022-05-10

### Added
- Initial implementation. Backport support for the following features:
  - 2.6 <= Python < 3.0: `builtins`.
  - 2.6 <= Python < 3.2: `ResourceWarning`, `datetime.timezone`,
    `os.makedirs`.
  - 2.6 <= Python < 3.4: `abc.ABC`, `tempfile.TemporaryDirectory`,
    `weakref.finalize`.
  - 3.0 <= Python < 3.2: `callable`.
  - 3.0 <= Python < 3.11: `basestring`.


[Unreleased]:
https://github.com/pylegacy/pylegacy/compare/v0.2.0...develop
[0.2.0]:
https://github.com/pylegacy/pylegacy/compare/v0.1.1...v0.2.0
[0.1.1]:
https://github.com/pylegacy/pylegacy/compare/v0.1.0...v0.1.1
[0.1.0]:
https://github.com/pylegacy/pylegacy/tree/v0.1.0
