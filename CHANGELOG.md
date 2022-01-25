# Changelog

All notable changes to this project will be documented in this file. The format
is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and the
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial implementation. Backport support for the following features:
  - 2.6 <= Python < 3.0: `builtins`.
  - 2.6 <= Python < 3.2: `ResourceWarning`, `os.makedirs`.
  - 3.0 <= Python < 3.2: `callable`, `datetime.timezone`.
  - 2.6 <= Python < 3.4: `abc.ABC`, `tempfile.TemporaryDirectory`,
    `weakref.finalize`.


[Unreleased]:
https://github.com/pylegacy/pylegacy/compare/master...develop
