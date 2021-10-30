"""Tests for :mod:`pylegacy.exceptions`."""

import sys
import unittest2 as unittest


class TestPyLegacyExceptions(unittest.TestCase):
    """Unittest class for :mod:`pylegacy.exceptions`."""

    def setUp(self):
        """Define the test scope variables."""

    def test_resourcewarning_available(self):
        """Test that :class:`ResourceWarning` exists with :mod:`pylegacy`."""

        import warnings
        from pylegacy.exceptions import ResourceWarning

        with self.assertWarns(ResourceWarning):
            warnings.warn("this is a ResourceWarning message", ResourceWarning)


if __name__ == "__main__":
    unittest.main()
