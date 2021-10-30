"""Legacy :mod:`exceptions` module."""
from __future__ import absolute_import

# Add temporary imports.
import sys as __sys

# Start with backports.
if __sys.version_info[:1] < (3,):

    from exceptions import *
    from exceptions import __doc__

    # Import backported warnings.
    from . builtins import ResourceWarning

else:

    msg = "cannot import name '{1}' from '{0}'".format(*__name__.rsplit(".", 1))
    raise ImportError(msg)

# Remove temporary imports.
del __sys
