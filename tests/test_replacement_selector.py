"""
Contains unit tests for verifying the correctness of the algorithms involving
simple replacement selection.
"""
from unittest import TestCase

from evored.selection import ReplacementSelector


class ReplacementSelectorTest(TestCase):
    """
    Test suite for ReplacementSelector.
    """

    def setUp(self):
        self.selector = ReplacementSelector()

    def test_replacement_selector(self):
        expected = [9, 8, 7, 6, 5, 9, 8, 7, 6, 5]
        ge_in = [5, 4, 6, 3, 7, 2, 8, 1, 9, 0]
        ge_out = []

        self.selector.select(ge_in, ge_out)
        self.assertEqual(expected, ge_out)
