"""
Since setuptools does [not support][2] [PEP 660][1] as of writing,
setup.py is required to install editable pyproject.toml-based project.
[1]: https://peps.python.org/pep-0660/
[2]: https://github.com/pypa/setuptools/issues/2816
"""
from setuptools import setup

setup()
