"""
Contains all classes and functions necessary to evaluate individual Redcode
warriors for fitness.
"""
from abc import ABCMeta, abstractmethod


class FitnessEvaluator(metaclass=ABCMeta):
    """
    Represents a mechanism to numerically evaluate Redcode warriors by
    computing an overall score based on each warrior's performance against
    any others.
    """

    @abstractmethod
    def evaluate(self, warriors, params):
        """
        Computes a score for each of the specified warriors that is used to
        determine whether the current iteration of their genome is worthwhile.

        Each element of the returned list of scores corresponds to the
        warrior at the index of the original argument list.

        Please note that contrary to the initial version of this project,
        the variable argument list contains the warriors as Python objects.
        Evaluators that use external programs - for example, PMARS - must
        perform any conversions (e.g. output to filenames) to appropriate
        mediums themselves.  All additional required arguments are expected
        to be included as user-selected parameters.

        :param warriors: The list of warriors to evaluate.
        :param params: A dictionary of parameters.
        :return: A list of fitness scores.
        """
        pass
