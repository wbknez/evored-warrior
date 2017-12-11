"""
Contains all classes and functions that perform miscellaneous tasks.
"""
import contextlib

import os
import tempfile

import shutil


@contextlib.contextmanager
def cd(newdir, cleanup=lambda: True):
    """
    Changes the current working directory to that of the specified directory
    (which for this project is a temporary) and executes the specified
    clean-up function before leaving scope.

    :param newdir: The temporary directory to use.
    :param cleanup: Whether or not to delete the temporary directory on exit.
    """
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)
        cleanup()


@contextlib.contextmanager
def tempdir():
    """
    Creates a temporary directory and returns the full path to it.

    :return: The path to a temporary directory.
    """
    dirpath = tempfile.mkdtemp()

    def cleanup():
        shutil.rmtree(dirpath)
        return True

    with cd(dirpath, cleanup):
        yield dirpath
