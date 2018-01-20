"""
Contains all classes and functions pertaining to methods of genome mutation.
"""
from abc import abstractmethod
from functools import partial
from random import random

from evored.evolution import EvolvingAlgorithm


class Mutator(EvolvingAlgorithm):
    """
    Represents a mechanism for altering a genome in some way, with the
    stipulation that such changes are made in an attempt to improve its
    overall fitness.
    """

    def evolve(self, genomes, pool, params):
        binding = partial(self.mutate, params=params)
        return pool.map(binding, genomes)

    @abstractmethod
    def mutate(self, genome, params):
        """
        Mutates the specified genome in some way, influenced by the specified
        user-selected parameters.

        All implementations of this method must determine if the specified
        genome is allowed to be mutated before any operations are performed.

        :param genome: The object to mutate.
        :param params: A dictionary of parameters.
        :return: A mutated genome.
        """
        pass


class HeapDownMutator(Mutator):
    """
    Represents an implementation of Mutator that applies a single pass of a
    heap-down operation to a genome, swapping the parent with the largest
    child.

    In terms of performance, this mutator is intended to strike a balance
    between modifying the genomes in a meaningful way without becoming bogged
    down by the potential pitfalls of an unknown tree structure.  As such,
    this mutator performs a single traversal from an arbitrary starting node
    - usually the root - and applies a heap-down operation at each additional
    node it encounters.  This allows the overall fitness of a genome to
    improve by moving better performing instructions further up the tree,
    but this effect is mediated due to the lack of percolation.

    As previously stated, this mutator may be configured to choose a random
    starting node instead of solely the root.  This has the effect of further
    mitigating any fitness increase structure alteration may bring.
    """

    def get_largest_child(self, node):
        """
        Computes which child of the specified node is the largest and returns
        it.

        :param node: The node to obtain the largest child from.
        :return: The largest child of a node.
        """
        if node.has_left() and not node.has_right():
            return node.left
        elif not node.has_left() and node.has_right():
            return node.right
        else:
            return node.left if node.left.item >= node.right.item else \
                node.right

    def heapify(self, node):
        """
        Performs a single heap-down operation on the specified node and its
        immediate children, selecting the largest child and replacing its
        parent as necessary.

        :param node: The node to apply a heap-down operation to.
        """
        chosen_child = self.get_largest_child(node)
        if node.item < chosen_child.item:
            node.swap_items(chosen_child)

    def mutate(self, genome, params):
        if random() > params["mutator.rate"]:
            return

        node = genome.root if params.get("mutator.root_only", True) else \
            genome.choose_node()

        queue = [node]
        while queue:
            current = queue.pop(0)
            self.heapify(current)
            if current.has_left() and not current.left.is_leaf():
                queue.append(current.left)
            if current.has_right() and not current.right.is_leaf():
                queue.append(current.right)
        return genome
