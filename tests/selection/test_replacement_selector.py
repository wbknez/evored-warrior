"""

"""
from random import shuffle
from unittest import TestCase

from math import ceil
from pathos.multiprocessing import ProcessPool

from evored.selection import ReplacementSelector
from tests import create_genomes


class ReplacementSelectorTest(TestCase):
    """

    """

    pool = ProcessPool(processes=2)
    """
    The process pool for testing.
    """

    def setUp(self):
        self.params = {}
        self.selector = ReplacementSelector()

    def tearDown(self):
        pass

    def test_replacement_selection_with_even_size_list(self):
        genomes = create_genomes(10)
        genomes.sort(reverse=True, key=lambda g: g.fitness)
        min_fitness = genomes[ceil(len(genomes) / 2)].fitness

        shuffle(genomes)
        results = self.selector.evolve(genomes, self.pool, self.params)

        self.assertEqual(len(results), len(genomes))
        for result in results:
            self.assertGreaterEqual(result.fitness, min_fitness)

    def test_replacement_selection_with_odd_size_list(self):
        genomes = create_genomes(21)
        genomes.sort(reverse=True, key=lambda g: g.fitness)
        min_fitness = genomes[ceil(len(genomes) / 2)].fitness

        shuffle(genomes)
        results = self.selector.evolve(genomes, self.pool, self.params)

        self.assertEqual(len(results), len(genomes))
        for result in results:
            self.assertGreaterEqual(result.fitness, min_fitness)

    def test_select_returns_current_node_and_copy(self):
        genomes = create_genomes(10)
        results = self.selector.select(genomes[0], genomes, self.params)

        self.assertEqual(len(results), 2)
        self.assertIs(results[0], genomes[0])
        self.assertIsNot(results[1], genomes[0])
        self.assertEqual(results[0], results[1])
