"""
Contains all classes and functions pertaining to methods of genome selection.
"""
from abc import ABCMeta, abstractmethod
from copy import copy
from math import ceil
from random import choice


class Selector(metaclass=ABCMeta):
    """
    Represents a mechanism for selecting poorly performing genomes and
    replacing them.
    """

    @abstractmethod
    def select(self, ge_in, ge_out, params=None):
        """
        Selects the best genomes from the specified list for continuation in
        some way, influenced by the specified user-selected parameters.

        Please note that input list is not intended to be modified.  All
        surviving genomes should be added to the output list only.  This is
        intended to reduce the number of list creations over the lifetime of
        this project.  This function may safely assume that the output list
        is cleared before use.

        Finally, the burden of implementing elitism falls on the caller,
        not this function.  As such, this function should neither consider
        the implications of nor perform elitism itself.

        :param ge_in: The list of genomes to select from.
        :param ge_out: The list of genomes that will survive to the next round.
        :param params: A dictionary of parameters.
        """
        pass


class ReplacementSelector(Selector):
    """
    Represents an implementation of Selector that replaces the bottom half of a
    list of genomes with copies from the top.
    """

    def select(self, ge_in, ge_out, params=None):
        if not params:
            params = {}

        current = 0
        half_size = ceil(len(ge_in) / 2)

        ge_in.sort(reverse=True)
        ge_out.extend(ge_in[:half_size])

        while len(ge_out) != len(ge_in):
            ge_out.append(copy(ge_in[current]))
            current += 1


class TournamentSelector(Selector):
    """
    Represents an implementation of Selector that performs an n-size
    random tournament to find the best genomes for selection.
    """

    def select(self, ge_in, ge_out, params=None):
        if not params:
            params = {}

        tourn_size = params.get("selector.tournament_size", 2)
        for i in range(0, len(ge_in)):
            best = None
            for t in range(0, tourn_size):
                chosen = choice(ge_in)
                if best is None or chosen > best:
                    best = chosen
            ge_out.append(copy(best))
