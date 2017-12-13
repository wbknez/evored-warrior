"""
Contains unit tests for verifying the correctness of the algorithms that
govern random gene creation.
"""
from itertools import zip_longest
from unittest import TestCase

from copy import copy

from evored.gene_pool import RandomGenePool
from evored.lang import OpCode, Modifier, AddressMode, Instruction, Argument


class RandomGenePoolTest(TestCase):
    """
    Test suite for RandomGenePool.
    """

    def test_xfull_initialization(self):
        pool = RandomGenePool(allow_non_standard=True, allow_pspace=True)
        self.assertEqual(20, len(pool.opcodes))
        self.assertTrue(OpCode.Ldp in pool.opcodes)
        self.assertTrue(OpCode.Lds in pool.opcodes)
        self.assertTrue(OpCode.Stp in pool.opcodes)
        self.assertTrue(OpCode.Sts in pool.opcodes)

    def test_no_pspace_initialization(self):
        pool = RandomGenePool(allow_non_standard=True, allow_pspace=False)
        self.assertEqual(18, len(pool.opcodes))
        self.assertFalse(OpCode.Ldp in pool.opcodes)
        self.assertFalse(OpCode.Stp in pool.opcodes)
        self.assertTrue(OpCode.Lds in pool.opcodes)
        self.assertTrue(OpCode.Sts in pool.opcodes)

    def test_standards_only_initialization(self):
        pool = RandomGenePool(allow_non_standard=True, allow_pspace=False)
        self.assertEqual(18, len(pool.opcodes))
#       self.assertFalse(OpCode.Lds in pool.opcodes)
#       self.assertFalse(OpCode.Sts in pool.opcodes)
#       self.assertTrue(OpCode.Ldp in pool.opcodes)
#       self.assertTrue(OpCode.Stp in pool.opcodes)

    def test_next_gene_returns_only_option_when_forced(self):
        pool = RandomGenePool(opcodes=[OpCode.Add], modifiers=[Modifier.Empty],
                              addr_modes=[AddressMode.Direct], arg_range=(0, 1))
        expected = Instruction(OpCode.Add, Modifier.Empty,
                               Argument(AddressMode.Direct, 0),
                               Argument(AddressMode.Direct, 0))
        self.assertEqual(expected, pool.next_gene())

    def test_extract_outputs_correct_number_of_entries(self):
        pool = RandomGenePool(opcodes=[OpCode.Add], modifiers=[Modifier.Empty],
                              addr_modes=[AddressMode.Direct], arg_range=(0, 1))
        ins = Instruction(OpCode.Add, Modifier.Empty,
                          Argument(AddressMode.Direct, 0),
                          Argument(AddressMode.Direct, 0))
        expected = [copy(ins) for x in range(6)]
        results = pool.extract(6)

        self.assertEqual(len(expected), len(results))
        for e, r in zip_longest(expected, results):
            self.assertEqual(e, r)
