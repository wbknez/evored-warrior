"""
Contains all classes and functions pertaining to methods of genome crossover.
"""
from abc import ABCMeta, abstractmethod


class Crossover(metaclass=ABCMeta):
    """
    Represents a mechanism for swapping portions of two genome's genetic
    information with each other.
    """

    @abstractmethod
    def cross(self, obj_a, obj_b, params):
        """
        Crosses the genetic material of the specified objects in some way,
        influenced by the specified user-selected parameters.

        :param obj_a: An object to perform crossover upon.
        :param obj_b: Another object to perform crossover upon.
        :param params: A dictionary of parameters.
        """
        pass
