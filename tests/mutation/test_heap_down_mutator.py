"""
Contains unit tests for verifying the correctness of the algorithms involving
heap-based mutation.
"""
from unittest import TestCase

from evored.genome import Genome
from evored.mutation import HeapDownMutator


class HeapDownMutatorTest(TestCase):
    """
    Test suite for HeapDownMutator.
    """

    def setUp(self):
        self.mutator = HeapDownMutator()
        self.params = {"mutator.rate": 1.0}

    def tearDown(self):
        pass

    def test_heap_down_using_simple_tree(self):
        genome = Genome([12, 40, 32])
        output = self.mutator.mutate(genome, self.params)

        expected = [40, 12, 32]
        results = [x.item for x in output]

        self.assertEqual(expected, results)

    def test_heap_down_works_when_only_one_child_exists(self):
        genome = Genome([12, 40])
        output = self.mutator.mutate(genome, self.params)

        expected = [40, 12]
        results = [x.item for x in output]

        self.assertEqual(expected, results)

    def test_heap_down_with_larger_tree(self):
        genome = Genome([1, 2, 3, 4, 5, 6, 7])
        output = self.mutator.mutate(genome, self.params)

        expected = [3, 5, 7, 4, 2, 6, 1]
        results = [x.item for x in output]

        self.assertEqual(expected, results)
