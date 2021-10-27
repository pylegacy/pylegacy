"""Import test for :mod:`pylegacy`."""
# pylint: disable=import-error
from __future__ import print_function

import re
import unittest2 as unittest


class TestPyLegacy(unittest.TestCase):
    """Unittest class for :mod:`pylegacy`."""

    def setUp(self):
        """Define the test scope variables."""

    def test_import(self):
        """Test that basic library import is working."""

        import pylegacy

        version = pylegacy.__version__
        self.assertTrue(isinstance(version, str))
        self.assertTrue(re.match(r"^(\d\.\d\.\d)(\+dev)?$", version))


if __name__ == "__main__":
    unittest.main()
