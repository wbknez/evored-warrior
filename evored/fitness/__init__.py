"""
Contains classes and functions related to fitness evaluation.
"""
from abc import ABCMeta


class Fitnessable(metaclass=ABCMeta):
    """
    Represents an object that contains a concept of fitness.

    Attributes:
        fitness (int): A fitness score.
    """

    def __init__(self, fitness=0):
        self.fitness = fitness

    def __eq__(self, other):
        if isinstance(other, Fitnessable):
            return self.fitness == other.fitness
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fitnessable):
            return self.fitness >= other.fitness
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fitnessable):
            return self.fitness > other.fitness
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fitnessable):
            return self.fitness <= other.fitness
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fitnessable):
            return self.fitness < other.fitness
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return repr(self.fitness)

    def __str__(self):
        return "(f:%i)" % self.fitness
