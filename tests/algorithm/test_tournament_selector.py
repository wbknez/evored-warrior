"""

"""
from copy import copy
from random import randint
from unittest import TestCase

from pathos.multiprocessing import ProcessPool

from evored.genome import Genome
from evored.algorithm.selection import TournamentSelector


class TournamentSelectorTest(TestCase):
    """
    Test suite for TournamentSelector.
    """

    pool = ProcessPool(processes=2)
    """
    The process pool for testing.
    """

    def setUp(self):
        self.params = {"selector.tournament_size": 4}
        self.selector = TournamentSelector()

    def tearDown(self):
        pass

    def test_basic_tournament_selection(self):
        genomes = [
            Genome(list(range(randint(1, 10))), 20),
            Genome(list(range(randint(1, 10))), 32),
            Genome(list(range(randint(1, 10))), 44),
            Genome(list(range(randint(1, 10))), 2),
        ]

        results = self.selector.select(None, genomes, self.params)
        self.assertEqual(genomes[2], results)

    def test_tournament_selection_in_parallel(self):
        genomes = [
            Genome(list(range(randint(1, 10))), 20),
            Genome(list(range(randint(1, 10))), 44),
            Genome(list(range(randint(1, 10))), 32),
            Genome(list(range(randint(1, 10))), 2),
        ]

        expected = [copy(genomes[1]) for _ in range(4)]
        results = self.selector.evolve(genomes, self.pool, self.params)

        self.assertEqual(len(results), 4)
        self.assertEqual(results, expected)
