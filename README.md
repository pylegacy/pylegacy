# pylegacy

This library aims to provide backports from Python newer versions into
abandoned Python versions.

The `pylegacy` package tree structure resembles that of the Python
standard libraries, i.e. `pylegacy` consists of `pylegacy.abc`,
`pylegacy.builtins`, `pylegacy.os`, and so on. If a backport is
available for a piece of missing functionality, it can be used by
importing the functionality from the `pylegacy` namespace.

For example, `os.makedirs` in Python 2.7 lacks the `exist_ok` argument,
first introduced in Python 3.2. To enable this functionality, one would
replace the following failing code snippet:
```python
import os
os.makedirs("example_folder", exist_ok=True)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: makedirs() got an unexpected keyword argument 'exist_ok'
```

with the following working code snippet:
```python
from pylegacy import os
os.makedirs("example_folder", exist_ok=True)
```
