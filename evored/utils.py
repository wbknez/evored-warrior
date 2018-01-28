"""
Contains all classes and functions that perform miscellaneous tasks.
"""
import contextlib

import os
import tempfile

import shutil


def flatten(llist):
    """
    Flattens the specified list, iterating over any sublists within and
    placing those elements into a new, larger list.

    :param llist: The list to flatten.
    :return: A new list containing the elements of all sublists.
    """
    return [item for sublist in llist for item in sublist]


@contextlib.contextmanager
def cd(new_dir, cleanup=lambda: True):
    """
    Changes the current working directory to that of the specified directory
    (which for this project is a temporary) and executes the specified
    clean-up function before leaving scope.

    :param new_dir: The temporary directory to use.
    :param cleanup: Whether or not to delete the temporary directory on exit.
    """
    prev_dir = os.getcwd()
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield
    finally:
        os.chdir(prev_dir)
        cleanup()


@contextlib.contextmanager
def tempdir():
    """
    Creates a temporary directory and returns the full path to it.

    :return: The path to a temporary directory.
    """
    dir_path = tempfile.mkdtemp()

    def cleanup():
        shutil.rmtree(dir_path)
        return True

    with cd(dir_path, cleanup):
        yield dir_path
