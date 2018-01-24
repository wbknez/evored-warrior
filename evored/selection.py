"""
Contains all classes and functions pertaining to methods of genome selection.
"""
from abc import abstractmethod
from functools import partial
from random import shuffle, sample, random, choice

from math import ceil

from copy import copy

from evored.evolution import EvolvingAlgorithm
from evored.utils import flatten


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


class ReplacementSelector(Selector):
    """
    Represents an implementation of Selector that replaces the lower half of a
    genome fitness distribution with the upper portion.
    """

    def evolve(self, genomes, pool, params):
        fixed_size = len(genomes)
        upper_bound = ceil(fixed_size / 2)

        genomes.sort(reverse=True)
        binding = partial(self.select, genomes=genomes, params=params)
        selected = flatten(pool.map(binding, genomes[:upper_bound]))

        if len(selected) == (len(genomes) + 1):
            del selected[-1]

        return selected

    def select(self, current, genomes, params):
        return [current, copy(current)]


class NoSelector(Selector):
    """
    Represents an implementation of Selector that does nothing.
    """

    def select(self, current, genomes, params):
        return current


class RouletteSelector(Selector):
    """
    Represents an implementation of Selector that uses stochastic acceptance to
    select genomes to allow into the next generation.
    """

    def evolve(self, genomes, pool, params):
        genomes.sort()
        binding = partial(self.select, genomes=genomes, params=params)
        return pool.map(binding, genomes)

    def select(self, current, genomes, params):
        while True:
            selected = choice(genomes)
            if random() < (selected.fitness / genomes[-1].fitness):
                return copy(selected)


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
        return copy(max(sample(genomes, params["selector.tournament_size"])))

