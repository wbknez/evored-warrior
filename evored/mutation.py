"""
Contains all classes and functions pertaining to methods of genome mutation.
"""
from abc import abstractmethod
from functools import partial

from evored.evolution import EvolvingAlgorithm


class Mutator(EvolvingAlgorithm):
    """
    Represents a mechanism for altering a genome in some way, with the
    stipulation that such changes are made in an attempt to improve its
    overall fitness.
    """

    def evolve(self, genomes, pool, params):
        binding = partial(self.mutate, params=params)
        return pool.map(binding, genomes)

    @abstractmethod
    def mutate(self, genome, params):
        """
        Mutates the specified genome in some way, influenced by the specified
        user-selected parameters.

        :param genome: The object to mutate.
        :param params: A dictionary of parameters.
        :return: A mutated genome.
        """
        pass
