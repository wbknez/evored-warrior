"""

"""
from random import randint
from unittest import TestCase

from evored.genome import Genome
from evored.selection import TournamentSelector


class TournamentSelectorTest(TestCase):
    """
    Test suite for TournamentSelector.
    """

    def setUp(self):
        self.params = {"selector.tournament_size": 4}
        self.selector = TournamentSelector()

    def tearDown(self):
        pass

    def test_basic_tournament_selection(self):
        genomes = [
            Genome(list(range(randint(0, 10))), 20),
            Genome(list(range(randint(0, 10))), 32),
            Genome(list(range(randint(0, 10))), 44),
            Genome(list(range(randint(0, 10))), 2),
        ]

        results = self.selector.select(genomes, self.params)
        self.assertEqual(genomes[2], results)
