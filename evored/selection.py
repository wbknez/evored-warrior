"""
Contains all classes and functions pertaining to methods of genome selection.
"""
from abc import ABCMeta, abstractmethod


class Selector(metaclass=ABCMeta):
    """
    Represents a mechanism for selecting poorly performing genomes and
    replacing them.
    """

    @abstractmethod
    def select(self, ge_in, ge_out, params):
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
