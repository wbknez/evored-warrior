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
    def cross(self, genome_a, genome_b, params):
        """
        Crosses the genetic material of the specified genomes in some way,
        influenced by the specified user-selected parameters.

        :param genome_a: A genome to perform crossover upon.
        :param genome_b: Another genome to perform crossover upon.
        :param params: A dictionary of parameters.
        :return: A list containing the genomes after crossover.
        """
        pass
