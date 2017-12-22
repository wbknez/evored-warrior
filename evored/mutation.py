"""
Contains all classes and functions pertaining to methods of genome mutation.
"""
from abc import ABCMeta, abstractmethod


class Mutator(metaclass=ABCMeta):
    """
    Represents a mechanism for altering a genome in some way, with the
    stipulation that such changes are made in an attempt to improve its
    overall fitness.
    """

    @abstractmethod
    def mutate(self, genome, params):
        """
        Mutates the specified genome in some way, influenced by the specified
        user-selected parameters.

        :param genome: The object to mutate.
        :param params: A dictionary of parameters.
        """
        pass


class HeapDownMutator(Mutator):
    """
    Represents an implementation of Mutator that applies a single pass of a
    heap-down operation to a genome, swapping the parent with the largest
    child.

    Please note that this implementation automatically assumes that genomes
    that it operates on were selected for mutation.  This algorithm is not
    intended, nor is it capable, of selectively mutating chromosomes.

    The only configurable element, which may be modified via a dictionary of
    parameters, is whether or not mutation begins at the root or at a
    randomly chosen node.  By default, the root is chosen for purposes of
    simplicity but random selection may help moderate the potentially drastic
    influence frequent mutation likely has.
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
        if not genome.root:
            raise ValueError("Cannot mutate - the genome is empty.")

        node = genome.root if params.get("mutator.heap.root", True) else \
            genome.choose_node()

        if node.is_leaf():
            return

        queue = [node]
        while queue:
            current = queue.pop(0)
            self.heapify(current)
            if current.has_left() and not current.left.is_leaf():
                queue.append(current.left)
            if current.has_right() and not current.right.is_leaf():
                queue.append(current.right)
