"""
Contains all classes and functions pertaining to methods of genome mutation.
"""
from abc import ABCMeta, abstractmethod


class Mutator(metaclass=ABCMeta):
    """
    Represents a mechanism for altering an arbitrary object (in this case,
    a genome or an instruction argument) in some way, with the stipulation
    that such changes are made in an attempt to improve its overall fitness.
    """

    @abstractmethod
    def mutate(self, obj, params):
        """
        Mutates the specified object in some way, influenced by the specified
        user-selected parameters.

        :param obj: The object to mutate.
        :param params: A dictionary of parameters.
        """
        pass
