"""Legacy :mod:`os` module."""
from __future__ import absolute_import

# Add temporary imports.
import sys as __sys

# Import `os` members.
from os import __dict__ as __dict
for __k, __v in __dict.items():
    if not (__k.startswith("__") and __k.endswith("__")) or __k == "__doc__":
        globals().update({__k: __v})
    del __k
    del __v
del __dict

# Start with backports.
if __sys.version_info[:2] < (3, 2):

    # Backport info:
    # - Python 3.2: first appeareance.
    def makedirs(name, mode=0o777, exist_ok=False):
        """makedirs(name [, mode=0o777][, exist_ok=False])

        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.
        """

        import os
        import errno

        exist_ok = bool(exist_ok)
        try:
            os.makedirs(name, mode)
        except OSError as err:
            if exist_ok and os.path.isdir(name) and err.errno == errno.EEXIST:
                return
            raise

# Remove temporary imports.
del __sys
