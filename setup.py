#! /usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa: E122
"""pylegacy -- Backports for abandoned Python versions."""

import io
import os
from setuptools import setup
from setuptools import find_packages
from src.pylegacy import __version__


def get_content(name, splitlines=False):
    """Return the file contents with project root as root folder."""

    here = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(here, name)
    with io.open(path, encoding="utf-8") as fd:
        content = fd.read()
    if splitlines:
        content = [row for row in content.splitlines() if row]
    return content


setup(**{
    "name":
        "pylegacy",
    "version":
        __version__,
    "license":
        "Python Software Foundation License",
    "description":
        "Backports for abandoned Python versions",
    "long_description":
        get_content("README.md"),
    "long_description_content_type":
        "text/markdown",
    "url":
        "https://github.com/pylegacy/pylegacy",
    "maintainer":
        "Víctor Molina García",
    "maintainer_email":
        "molinav@users.noreply.github.com",
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    "keywords": [
        "compatibility",
        "backports",
        "legacy",
    ],
    "package_dir":
        {"": "src"},
    "packages":
        find_packages(where="src"),
    "python_requires":
        ", ".join([
            ">=2.6",
            "!=3.0.*",
            "!=3.1.*",
            "<3.11",
        ]),
    "extras_require": {
        "lint":
            get_content("requirements-lint.txt", splitlines=True),
        "test":
            get_content("requirements-test.txt", splitlines=True),
    },
    "project_urls": {
        "Bug Tracker":
            "https://github.com/pylegacy/pylegacy/issues",
        "Source":
            "https://github.com/pylegacy/pylegacy",
    },
})
