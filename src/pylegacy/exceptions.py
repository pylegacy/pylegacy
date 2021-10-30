"""Legacy :mod:`exceptions` module."""
from __future__ import absolute_import

# Add temporary imports.
import sys as __sys

# Import `exceptions` members.
from . builtins import __dict__ as __builtins_dict
for __k, __v in __builtins_dict.items():
    if any(list(map(__k.endswith, ["Exception", "Error", "Warning"]))):
        globals().update({__k: __v})
    del __k
    del __v
del __builtins_dict

# Copy the original module docstring for Python 2.
if __sys.version_info[:1] < (3,):
    from exceptions import __doc__ as __exceptions_doc
    __doc__ = __exceptions_doc
    del __exceptions_doc

# Remove temporary imports.
del __sys
