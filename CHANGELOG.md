# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog], and the project adheres to
[Semantic Versioning].

[Keep a Changelog]:
https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]:
https://semver.org/spec/v2.0.0.html


## [Unreleased]

### Changed
- Update upper pin for `flake8` to 5.1 in lint requirements.

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
https://github.com/pylegacy/pylegacy/compare/master...develop
[0.1.0]:
https://github.com/pylegacy/pylegacy/tree/v0.1.0
