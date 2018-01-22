"""
Contains unit tests for verifying the correctness of crossover pair extraction.
"""
from unittest import TestCase

from evored.crossover import Crossover
from tests import create_genomes


class CrossoverTest(TestCase):
    """
    Test suite for Crossover.
    """


    class EmptyCrossover(Crossover):
        """
        Represents a test implementation of Crossover that does nothing.
        """

        def cross(self, genome_a, genome_b, params):
            pass

    def setUp(self):
        self.crossover = CrossoverTest.EmptyCrossover()

    def tearDown(self):
        pass

    def test_crossing_pairs_with_probability_of_one_and_even_size(self):
        genomes = create_genomes(10)
        params = {"crossover.rate": 1.0}

        gen_a, gen_b = self.crossover.extract_crossing_pairs(genomes, params)

        self.assertEqual(len(gen_a), 5)
        self.assertEqual(len(gen_b), 5)
        self.assertEqual(len(genomes), 0)

    def test_crossing_pairs_with_probability_of_one_and_odd_size(self):
        genomes = create_genomes(11)
        params = {"crossover.rate": 1.0}

        gen_a, gen_b = self.crossover.extract_crossing_pairs(genomes, params)

        self.assertEqual(len(gen_a), 5)
        self.assertEqual(len(gen_b), 5)
        self.assertEqual(len(genomes), 1)

    def test_crossing_pairs_with_probability_of_zero_and_even_size(self):
        genomes = create_genomes(10)
        params = {"crossover.rate": 0.0}

        gen_a, gen_b = self.crossover.extract_crossing_pairs(genomes, params)

        self.assertEqual(len(gen_a), 0)
        self.assertEqual(len(gen_b), 0)
        self.assertEqual(len(genomes), 10)

    def test_crossing_pairs_with_probability_of_zero_and_odd_size(self):
        genomes = create_genomes(11)
        params = {"crossover.rate": 0.0}

        gen_a, gen_b = self.crossover.extract_crossing_pairs(genomes, params)

        self.assertEqual(len(gen_a), 0)
        self.assertEqual(len(gen_b), 0)
        self.assertEqual(len(genomes), 11)
