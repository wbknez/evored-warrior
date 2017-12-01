"""
Contains all classes and functions pertaining to the random generation of
Redcode instructions.
"""
from abc import ABCMeta, abstractmethod


class GenePool(metaclass=ABCMeta):
    """
    Represents a mechanism for randomly creating genes.

    For purposes of this project, a "gene" is a single Redcode instruction
    that is not coupled to a fitness score.
    """

    @abstractmethod
    def next_gene(self):
        """
        Creates and returns a new random gene.

        :return: A new random gene.
        """
        pass
