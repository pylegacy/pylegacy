"""Tests for :mod:`pylegacy.builtins`."""
# pylint: disable=import-error
# flake8: noqa: F821
from __future__ import print_function

import sys
import unittest2 as unittest


class TestPyLegacyBuiltins(unittest.TestCase):
    """Unittest class for :mod:`pylegacy.builtins`."""

    def setUp(self):
        """Define the test scope variables."""

    @unittest.skipIf(sys.version_info[:2] >= (3, 2), reason="no backport")
    def test_resourcewarning_missing(self):
        """Test that :class:`ResourceWarning` does not exist."""

        def test_callable():
            """Helper function."""
            return ResourceWarning  # pylint: disable=undefined-variable

        self.assertRaises(NameError, test_callable)

    def test_resourcewarning_available(self):
        """Test that :class:`ResourceWarning` exists with :mod:`pylegacy`."""

        import warnings
        from pylegacy.builtins import ResourceWarning

        with self.assertWarns(ResourceWarning):
            warnings.warn("this is a ResourceWarning message", ResourceWarning)


if __name__ == "__main__":
    unittest.main()
