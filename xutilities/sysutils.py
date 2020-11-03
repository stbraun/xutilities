# -*- coding: utf-8 -*-

"""System utilities."""

import os
from pathlib import Path


def which(executable: str) -> Path:
    """Looks in $PATH for `executable`.

    :param executable: name of executable to look up.
    :type executable: str
    :return: absolute path of executable.
    :rtype: pathlib.Path
    :raises Exception: if executable not found in path.
    """
    for exec_path in os.get_exec_path():
        path = Path(exec_path) / executable

        if path.exists():
            return path.absolute()
    raise Exception(f'{executable} not found')


def get_venv() -> Path:
    """Determine path to active virtual environment.

    :return: path to virtual environment.
    :rtype: pathlib.Path
    :raises Exception: if no virtual environment was found.
    """
    path = which('python').parent.parent
    venv_markers = [path / 'pyvenv.cfg', path / 'conda-meta']
    if not any([marker.exists() for marker in venv_markers]):
        raise Exception("Not running in virtual environment!")
    return path
