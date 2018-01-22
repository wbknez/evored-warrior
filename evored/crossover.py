"""
Contains all classes and functions pertaining to methods of genome crossover.
"""
from abc import abstractmethod
from functools import partial
from random import random, shuffle

from evored.evolution import EvolvingAlgorithm
from evored.utils import flatten


class Crossover(EvolvingAlgorithm):
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

    def evolve(self, genomes, pool, params):
        shuffle(genomes)
        pair_a, pair_b = self.extract_crossing_pairs(genomes, params)

        binding = partial(self.cross, params=params)
        return genomes + flatten(pool.map(binding, pair_a, pair_b))

    def extract_crossing_pairs(self, genomes, params):
        """
        Iterates over the specified list of genomes and determines whether or
        not each pair therein will be subjected to crossover according to a
        user-specied rate.

        :param genomes: The list of genomes to extract crossover pairs from.
        :param params: The dictionary of user-specified parameters.
        :return: Two lists of genomes to facilitate element-wise crossover.
        """

        crossing_pairs = []
        for i in range(0, len(genomes) - 1, 2):
            if random() < params["crossover.rate"]:
                crossing_pairs.append(genomes.pop(i))
                crossing_pairs.append(genomes.pop(i + 1))
        half_width = len(crossing_pairs) // 2
        return [crossing_pairs[:half_width], crossing_pairs[half_width:]]


class UniformCrossover(Crossover):
    """
    Represents an implementation of Crossover that exchanges genetic
    information between two genomes chromosome by chromosome using a uniform
    probability.
    """

    def cross(self, genome_a, genome_b, params):
        for a, b in zip(genome_a, genome_b):
            if random() < params["crossover.uniform_rate"]:
                a.swap_items(b)
        return [genome_a, genome_b]
