"""
Contains classes and functions concerned with obtaining fitness scores from a
Core Wars simulation.
"""
from abc import ABCMeta, abstractmethod


class ScoringException(Exception):
    """
    Represents an exception that is thrown when attempting to score the
    fitness of a list of warriors.
    """

    pass


class ScoreProvider(metaclass=ABCMeta):
    """
    Represents a mechanism to numerically determine the fitness of Redcode
    warriors by computing an overall score based on each warrior's
    performance against one another.
    """

    @abstractmethod
    def calculate(self, warriors, file_prefix, params):
        """
        Computes a score for each of the specified warriors that is used to
        determine whether the current iteration of their genome is worthwhile.

        Each element of the returned list of scores corresponds to the
        warrior at the index of the original argument list.

        Unlike earlier implementations of this project, the list of warriors
        represents the actual instruction lists.  It is up to deriving
        classes to correctly (and safely) output any required source code
        using the specified prefix as necessary.

        :param warriors: The list of warriors to evaluate.
        :param file_prefix: The prefix to use when creating Redcode source
        files (to avoid being overwritten by other processes).  Pure
        simulation implementations may ignore this.
        :param params: A dictionary of parameters.
        :return: A list of fitness scores.
        :raise ScoringException: If there was a problem evaluating the warriors.
        """
        pass
