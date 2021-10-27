"""Tests for :mod:`pylegacy.os`."""
# pylint: disable=import-error
from __future__ import print_function

import sys
import unittest2 as unittest


class TestPyLegacyOs(unittest.TestCase):
    """Unittest class for :mod:`pylegacy.os`."""

    def setUp(self):
        """Define the test scope variables."""

    @unittest.skipIf(sys.version_info[:2] >= (3, 2), reason="no backport")
    def test_os_makedirs_error_args(self):
        """Test that :func:`os.makedirs` does not have `exist_ok` arg."""

        import os
        self.assertRaises(TypeError, os.makedirs, "dummy", 511, True)

    @unittest.skipIf(sys.version_info[:2] >= (3, 2), reason="no backport")
    def test_os_makedirs_error_kwargs(self):
        """Test that :func:`os.makedirs` does not have `exist_ok` kwarg."""

        import os
        self.assertRaises(TypeError, os.makedirs, "dummy", exist_ok=True)

    def test_pylegacy_os_makedirs(self):
        """Test usage of :func:`pylegacy.os.makedirs`."""

        import shutil
        import tempfile
        from pylegacy import os

        tmpdir = tempfile.mkdtemp()
        testdir = os.path.join(tmpdir, "dummy", "folder")

        try:
            # Test that the dummy folder does not exist.
            self.assertFalse(os.path.isdir(testdir))
            # Test creation of dummy folder.
            ret = os.makedirs(testdir)
            self.assertIs(ret, None)
            self.assertTrue(os.path.isdir(testdir))
            # Test `makedirs` raising error with `exist_ok` not set.
            self.assertRaises(OSError, os.makedirs, testdir)
            # Test `makedirs` raising error with `exist_ok` set to False.
            self.assertRaises(OSError, os.makedirs, testdir, exist_ok=False)
            # Test `makedirs` skipping error with `exist_ok` set to True.
            ret = os.makedirs(testdir, exist_ok=True)
            self.assertIs(ret, None)
        finally:
            shutil.rmtree(tmpdir)


if __name__ == "__main__":
    unittest.main()
