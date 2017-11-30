"""
Contains all classes and functions for creating and working with an
unstructured binary tree.
"""
import itertools
from copy import copy
from random import random, randrange


def _compare_items(a, b):
    """
    Compares the items of the specified nodes.

    In particular, this function will:
        - return True if both nodes are null.
        - return False if one node is null and the other is not.
        - return the comparison of each node's items, otherwise.

    :param a: A node to compare.
    :param b: Another node to compare.
    :return: Whether or not the items of two nodes are equivalent.
    """
    if a is None and b is None:
        return True
    elif (a is None and b is not None) or (a is not None and b is None):
        return False
    return a.item == b.item


def _get_item(node):
    """
    Returns the item element of the specified node if [the node] is not null.

    :param node: The node to extract the item from.
    :return: A node's item.
    """
    return node.item if node is not None else None


class Node:
    """
    Represents a single node in an unstructured binary tree.

    Attributes:
        item (object): The item contained in this node.
        left (Node): The left child of this node.
        parent (Node): The parent of this node.
        right (Node): The right child of this node.
    """

    def __init__(self, item, parent=None, left=None, right=None):
        self.item = item
        self.left = left
        self.parent = parent
        self.right = right

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.item == other.item and \
                   _compare_items(self.left, other.left) and \
                   _compare_items(self.parent, other.parent) and \
                   _compare_items(self.right, other.right)
        return NotImplemented

    def __hash__(self):
        return hash((self.item, _get_item(self.left), _get_item(self.parent),
                     _get_item(self.right)))

    def __ne__(self, other):
        return not self == other

    def choose_child(self):
        """
        Randomly chooses a child.

        Children are chosen using common-sense rules.  If either child is
        absent then the other is chosen and if none are present then None is
        return.  Finally, in the case of two children a random roll is
        conducted between 0 and 1 and the left child is chosen if that roll
        is less than 0.5 otherwise the right is returned.

        :return: A randomly chosen child.
        """
        if self.is_leaf():
            return None
        elif self.has_left() and not self.has_right():
            return self.left
        elif not self.has_left() and self.has_right():
            return self.right
        return self.left if random.uniform(0, 1) < 0.5 else self.right

    def has_left(self):
        """
        Returns whether or not this node has a left child.

        :return: Whether or not there is a left child.
        """
        return self.left is not None

    def has_right(self):
        """
        Returns whether or not this node has a right child.

        :return: Whether or not there is a right child.
        """
        return self.right is not None

    def is_full(self):
        """
        Returns whether or not this node has both children.

        :return: Whether or not there are two children.
        """
        return self.left is not None and self.right is not None

    def is_leaf(self):
        """
        Returns whether or not this node has no children.

        :return: Whether or not there are no children.
        """
        return self.left is None and self.right is None

    def is_node(self):
        """
        Returns whether or not this node has any children.

        :return: Whether or not there is at least one child.
        """
        return self.left is not None or self.right is not None

    def replace_child(self, child, node):
        """
        Replaces the specified child of this node with the specified node.

        Please note that this function does not reparent either the child or
        the replacement node.

        :param child: The child to replace.
        :param node: The node to use as a replacement.
        :raise ValueError: If the child is null or cannot be identified as a
        child of this node.
        """
        if child is None:
            raise ValueError("Child must not be null.")

        if child is self.left:
            self.left = node
        elif child is self.right:
            self.right = node
        else:
            raise ValueError("Child does not belong to this node.")

    def swap_children(self):
        """
        Swaps the placement of this node's children with each other,
        effectively swapping each child's branch with the other.
        """
        temp = self.left
        self.left = self.right
        self.right = temp

    def swap_places(self, node):
        """
        Swaps this node with the specified node, each replacing the other's
        position in their respective branch while keeping any sub-branches
        intact and unaltered.

        This function is identical to a branch swap.

        :param node: The node to swap with.
        """
        parent_a = self.parent
        parent_b = node.parent

        if (parent_a and parent_b) and (parent_a is parent_b):
            self.parent.swap_children()
            return

        if parent_a:
            parent_a.replace_child(self, node)
        if parent_b:
            parent_b.replace_child(node, self)

        self.parent = parent_b
        node.parent = parent_a


class Tree:
    """
    Represents an unstructured binary tree.

    Attributes:
        root (Node): The root node of this tree.
    """

    def __init__(self, items = None):
        self.root = None

        if not items is None:
            self.build(items)

    def __copy__(self):
        tree = Tree()
        tree.root = Node(copy(self.root.item))

        source = [self.root]
        dest = [tree.root]

        while source:
            s = source.pop(0)
            d = dest.pop(0)

            if s.has_left():
                source.append(s.left)
                d.left = Node(copy(s.left.item), parent=d)
                dest.append(d.left)
            if s.has_right():
                source.append(s.right)
                d.right = Node(copy(s.right.item), parent=d)
                dest.append(d.right)
        return tree

    def __eq__(self, other):
        if isinstance(other, Tree):
            for s, t in itertools.zip_longest(self, other):
                if not s == t:
                    return False
            return True
        return NotImplemented

    def __iter__(self):
        """
        Creates a generator that returns the nodes of this tree in
        breadth-first order.

        :return: The nodes of this tree in breadth-first order.
        """
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            yield current

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def build(self, items):
        """
        Fills out this tree in breadth-first order using the specified list
        of items as elements.

        :param items: The items to fill the tree with.
        """
        if self.root is not None:
            ValueError("Tree is already built.")

        self.root = Node(items[0])
        queue = [self.root]

        for item in itertools.islice(items, 1, len(items)):
            if queue[0].is_full():
                queue.pop(0)
            current = queue[0]

            if not current.has_left():
                current.left = Node(item=item, parent=current)
                queue.append(current.left)
            elif not current.has_right():
                current.right = Node(item=item, parent=current)
                queue.append(current.right)

    def choose_item(self):
        """
        Choose a random item from this tree.

        This function is a simple wrapper around choose_node() and therefore has
        the same performance characteristics.

        :return: The item from a randomly chosen node.
        """
        node = self.choose_node()
        return node.item if node is not None else None

    def choose_node(self):
        """
        Chooses a random node from this tree.

        This function is O(n) since, for this project, the number of nodes
        will always be unknown.

        :return: A randomly chosen node.
        """
        if not self.root:
            return None

        count = 0
        selected = None

        for node in self:
            count += 1
            if randrange(0, count) == 0:
                selected = node
        return selected

    def is_empty(self):
        """
        Determines whether or not this tree is empty.

        :return: Whether or not this tree is devoid of nodes.
        """
        return not self.root

    def random_walk(self):
        """
        Performs a "random walk" starting at the root node, randomly choosing
        the next child to walk to.

        Please note that this function returns a list of items, not nodes.
        In this project there is a strict functional separation between the tree
        structure and the value each node contains.

        :return: A list of items obtained from the walk.
        """
        items = []
        current = self.root

        while current:
            items.append(current.item)
            current = current.choose_child()
        return items
