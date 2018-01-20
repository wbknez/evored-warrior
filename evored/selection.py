"""
Contains all classes and functions pertaining to methods of genome selection.
"""
from abc import abstractmethod
from functools import partial

from evored.evolution import EvolvingAlgorithm


class Selector(EvolvingAlgorithm):
    """
    Represents a mechanism for selecting poorly performing genomes and
    replacing them.
    """

    def evolve(self, genomes, pool, params):
        binding = partial(self.select, genomes=genomes, params=params)
        return pool.map(binding, genomes)

    @abstractmethod
    def select(self, genomes, params):
        """
        Selects the best genomes from the specified list for continuation in
        some way, influenced by the specified user-selected parameters.

        Finally, the burden of implementing elitism falls on the caller,
        not this function.  As such, this function should neither consider
        the implications of nor perform elitism itself.

        :param genomes: The list of genomes to select from.
        :param params: A dictionary of parameters.
        :return: One or more genomes selected for continued evolution.
        """
        pass
