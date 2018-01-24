"""
Contains unit tests to verify that uniform crossover works correctly.
"""
from copy import copy
from random import randint
from unittest import TestCase

from pathos.multiprocessing import ProcessPool

from evored.crossover import UniformCrossover
from evored.genome import Genome
from tests import create_genomes


class UniformCrossoverTest(TestCase):
    """
    Test suite for UniformCrossover.
    """

    pool = ProcessPool(processes=2)
    """
    The process pool for testing.
    """

    def setUp(self):
        self.crossover = UniformCrossover()
        self.params = {"crossover.rate": 1.0,
                       "crossover.uniform_rate": 1.0}

    def test_cross_swaps_all_nodes_correctly(self):
        genome_a = Genome([x for x in range(0, 10)], randint(0, 100))
        genome_b = Genome([x for x in range(20, 30)], randint(0, 100))

        expected = [
            Genome([x for x in range(20, 30)], genome_a.fitness),
            Genome([x for x in range(0, 10)], genome_b.fitness)
        ]
        results = self.crossover.cross(genome_a, genome_b, self.params)
        self.assertEqual(expected, results)

    def test_uniform_crossover_in_parallel(self):
        genomes = create_genomes(10)
        fitness_scores = [x.fitness for x in genomes]

        expected = [copy(g) for g in genomes]
        results = self.crossover.evolve(genomes, self.pool, self.params)

        for genome, result in zip(genomes, results):
            self.assertEqual(genome.fitness, result.fitness)
        for i in range(0, len(genomes), 2):
            self.assertEqual(expected[i], results[i + 1])
            self.assertEqual(expected[i + 1], results[i])
