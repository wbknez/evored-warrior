"""
Contains all classes and functions pertaining to methods of genome selection.
"""
from abc import abstractmethod
from functools import partial
from random import shuffle, sample, random, choice

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
    def select(self, current, genomes, params):
        """
        Selects the best genomes from the specified list for continuation in
        some way, influenced by the specified user-selected parameters.

        Finally, the burden of implementing elitism falls on the caller,
        not this function.  As such, this function should neither consider
        the implications of nor perform elitism itself.

        :param current: The current genome (used as an index placeholder).
        :param genomes: The list of genomes to select from.
        :param params: A dictionary of parameters.
        :return: One or more genomes selected for continued evolution.
        """
        pass


class RouletteSelection(Selector):
    """
    An implementation of {@link SelectionFunction} that uses stochastic
    acceptance to select genomes to allow into the next generation.
    """

    def evolve(self, genomes, pool, params):
        sorted(genomes)
        binding = partial(self.select, genomes=genomes, params=params)
        return pool.map(binding, genomes)

    def select(self, current, genomes, params):
        while True:
            selected = choice(genomes)
            if random() < (selected.fitness / genomes[-1].fitness):
                return selected


class TournamentSelector(Selector):
    """
    Represents an implementation of Selector that performs an n-size
    random tournament to find the best genomes for selection.
    """

    def evolve(self, genomes, pool, params):
        shuffle(genomes)
        binding = partial(self.select, genomes=genomes, params=params)
        return pool.map(binding, genomes)

    def select(self, current, genomes, params):
        return max(sample(genomes, params["selector.tournament_size"]))

