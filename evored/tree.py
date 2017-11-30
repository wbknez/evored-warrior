"""
Contains all classes and functions for creating and working with an
unstructured binary tree.
"""


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

    def __hash__(self):
        return hash((self.item, _get_item(self.left), _get_item(self.parent),
                     _get_item(self.right)))

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
