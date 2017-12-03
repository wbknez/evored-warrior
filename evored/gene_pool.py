"""
Contains all classes and functions pertaining to the random generation of
Redcode instructions.
"""
from abc import ABCMeta, abstractmethod
from random import choice, randrange

from evored.lang import OpCode, Modifier, AddressMode, Instruction, Argument


class GenePool(metaclass=ABCMeta):
    """
    Represents a mechanism for randomly creating genes.

    For purposes of this project, a "gene" is a single Redcode instruction
    that is not coupled to a fitness score.
    """

    def extract(self, count):
        """
        Creates a list of new genes with the specified size.

        :param count: The number of genes to extract from the pool.
        :return: A list of new genes.
        """
        return [self.next_gene for _ in range(0, count)]

    @abstractmethod
    def next_gene(self):
        """
        Creates and returns a new random gene.

        :return: A new random gene.
        """
        pass


class RandomGenePool(GenePool):
    """
    Represents an implementation of GenePool that randomly chooses from a
    collection of operation codes, modifiers, addressing modes, and argument
    ranges to construct a single gene, or Redcode instruction.

    Attributes:
        addr_modes (list): The list of available addressing modes.
        arg_range (tuple): The range of values an argument may have.
        modifiers (list): The list of available instruction modifiers.
        opcodes (list): The list of available operation codes.
    """

    def __init__(self, opcodes=list(OpCode), modifiers=list(Modifier),
                 addr_modes=list(AddressMode), arg_range=(0, 8000)):
        super().__init__()
        self.opcodes = opcodes
        self.modifiers = modifiers
        self.addr_modes = addr_modes
        self.arg_range = arg_range

    def next_gene(self):
        return Instruction(choice(self.opcodes), choice(self.modifiers),
                           Argument(choice(self.addr_modes),
                                    randrange(self.arg_range)),
                           Argument(choice(self.addr_modes),
                                    randrange(self.arg_range)))
