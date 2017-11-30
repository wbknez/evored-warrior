"""
Contains unit tests for verifying correctness of fitness-related algorithms.
"""
from random import randint
from unittest import TestCase

from evored.genome import Fitnessable


class TestFitness(Fitnessable):
    """
    A test implementation of Fitnessable.
    """

    def __init__(self, fitness=0):
        super().__init__(fitness)


class FitnessableTest(TestCase):
    """
    Test suite for Fitnessable.
    """

    def test_ordering(self):
        objs = []

        for value in range(0, 100):
            objs.append(TestFitness(randint(0, 10000)))

        objs.sort(key=lambda f: f.fitness)

        for i in range(1, len(objs)):
            self.assertTrue(objs[i].fitness >= objs[i - 1].fitness)
