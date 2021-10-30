"""Legacy :mod:`builtins` module."""
from __future__ import absolute_import

# Add temporary imports.
import sys as __sys

# Import `builtins` members.
try:
    from builtins import __dict__ as __dict
except ImportError:
    from __builtin__ import __dict__ as __dict
for __k, __v in __dict.items():
    if not (__k.startswith("__") and __k.endswith("__")) or __k == "__doc__":
        globals().update({__k: __v})
    del __k
    del __v
del __dict

# Remove temporary imports.
del __sys
