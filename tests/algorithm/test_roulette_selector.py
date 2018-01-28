"""
Contains unit tests for ensuring the correctness of roulette genome selection.
"""
from unittest import TestCase

from pathos.multiprocessing import ProcessPool

from evored.genome import Genome
from evored.algorithm.selection import RouletteSelector


class RouletteSelectorTest(TestCase):
    """
    Test suite for RouletteSelector.
    """

    pool = ProcessPool(processes=2)
    """
    The process pool for testing.
    """

    def setUp(self):
        self.params = {}
        self.selector = RouletteSelector()

    def tearDown(self):
        pass

    def test_roulette_selection_in_parallel(self):
        genomes = [Genome([1], 11) for _ in range(10)]
        results = self.selector.evolve(genomes, self.pool, self.params)

        self.assertEqual(len(results), 10)
        for genome, result in zip(genomes, results):
            self.assertEqual(result, genome)

    def test_selector_returns_single_element_for_single_element_list(self):
        genomes = [Genome([1], 11)]
        results = self.selector.select(genomes[0], genomes, self.params)
        self.assertEqual(results, genomes[0])
