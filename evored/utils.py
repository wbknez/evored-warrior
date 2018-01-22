"""
Contains all classes and functions that perform miscellaneous tasks.
"""
import contextlib

import os
import tempfile

import shutil
from abc import ABCMeta, abstractmethod


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


class FilenameGenerator(metaclass=ABCMeta):
    """
    Represents a mechanism to reate new, unique names for use as temporary
    file descriptors.
    """

    @abstractmethod
    def next_file(self):
        """
        Creates and returns a new file name for use.

        :return: A new file name.
        """
        pass


class SequentialFilenameGenerator(FilenameGenerator):
    """
    Represents an implementation of FilenameGenerator that produces file
    names based on simple, incremental scheme.
    """

    def __init__(self, prefix="__temp__file__", ext="RED"):
        self.ext = ext
        self.idx = 0
        self.prefix = prefix

    def next_file(self):
        self.idx += 1
        return self.prefix + str(self.idx) + "." + self.ext


class FileCache:
    """
    Represents a mechanism for creating, caching, and reusing temporary file
    names.
    """

    def __init__(self, generator):
        self.cache = []
        self.generator = generator

    def __iter__(self):
        for cached in self.cache:
            yield cached

    def borrow(self):
        return self.cache.pop(0) if self.cache else self.generator.next_file()

    def reuse(self, file):
        self.cache.append(file)

    def reuse_all(self, files):
        self.cache.extend(files)
