"""
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

    def __repr__(self):
        return repr(self.fitness)

    def __str__(self):
        return "(f:%i)" % self.fitness
