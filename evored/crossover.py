"""
Contains all classes and functions pertaining to methods of genome crossover.
"""
from abc import ABCMeta, abstractmethod
from random import uniform


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
        """
        pass


class UniformCrossover(Crossover):
    """
    Represents an implementation of Crossover that exchanges the genetic
    information of two genomes using a uniform probability.
    """

    def cross(self, genome_a, genome_b, params):
        cross_rate = params.get("crossover.uniform_rate", 0.5)
        for a, b in genome_a, genome_b:
            if uniform(0, 1) < cross_rate:
                a.swap_items(b)
