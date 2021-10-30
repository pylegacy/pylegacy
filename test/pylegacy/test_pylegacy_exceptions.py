"""Tests for :mod:`pylegacy.exceptions`."""

import sys
import unittest2 as unittest


class TestPyLegacyExceptions(unittest.TestCase):
    """Unittest class for :mod:`pylegacy.exceptions`."""

    def setUp(self):
        """Define the test scope variables."""

    @unittest.skipIf(sys.version_info[:2] >= (3, 2), reason="no backport")
    def test_resourcewarning_missing(self):
        """Test that :class:`ResourceWarning` does not exist."""

        def test_callable():
            """Helper function."""
            # pylint: disable=undefined-variable
            return ResourceWarning  # noqa: F821

        self.assertRaises(NameError, test_callable)

    def test_resourcewarning_available(self):
        """Test that :class:`ResourceWarning` exists with :mod:`pylegacy`."""

        import warnings
        from pylegacy.exceptions import ResourceWarning

        with self.assertWarns(ResourceWarning):
            warnings.warn("this is a ResourceWarning message", ResourceWarning)


if __name__ == "__main__":
    unittest.main()
