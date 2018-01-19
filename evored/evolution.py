"""
Contains all classes and functions designed to make a uniform API for
performing different evolutionary operations on a list of genomes.
"""
from abc import abstractmethod, ABCMeta


class EvolvingAlgorithm(metaclass=ABCMeta):
    """
    Represents a single facet of a genetic algorithm that alters,
    reorganizes, or reconstitutes a list of genomes with the assistance of
    parallel processing.

    For this project, the pieces of the overall algorithm can be broken up
    into one of three tasks:
        1. Selection, or the determination of the most (currently) fit genomes.
        2. Mutation, or the alteration of genomes to increase fitness.
        3. Crossover, or the exchange of genetic data between genomes to
        produce diversity.

    This interface is intended to define a uniform usage pattern for all
    portions of this project in order to facilitate parallel processing.
    Each algorithm is expected to use a shared process pool and offload as
    much work as possible to it.  This uniform usage pattern hides the
    different argumentation each task may require, allowing the solver to
    blindly call as necessary.
    """

    @abstractmethod
    def evolve(self, genomes, pool, params):
        """
        Performs arbitrary evolutionary logic on the specified list of
        genomes, using the specified pool of processes to do so, with the
        specified dictionary of user-specified parameters.

        Every implementation of this method is required to return a new list
        of modified genomes - regardless of the logic used to do so - in
        order to conform to expected parallel processing workflow.

        :param genomes: The list of genomes to evolve in some way.
        :param pool: The pool of processes to use for work.
        :param params: The dictionary of user-specified parameters.
        :return: A new list of modified genomes.
        """
        pass
