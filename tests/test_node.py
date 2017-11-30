"""
Contains unit tests for verifying correctness of Node-related algorithms.
"""
from unittest import TestCase

from evored.tree import Node


class NodeTest(TestCase):
    """
    Test suite for Node.
    """
    
    def test_has_left(self):
        node = Node(32)
        node.left = Node(100, parent=node)
        self.assertTrue(node.has_left())
        
    def test_has_left_is_not_true_when_there_is_no_left_child(self):
        node = Node(32)
        self.assertFalse(node.has_left())

    def test_has_right(self):
        node = Node(32)
        node.right = Node(100, parent=node)
        self.assertTrue(node.has_right())

    def test_has_right_is_not_true_when_there_is_no_right_child(self):
        node = Node(32)
        self.assertFalse(node.has_right())

    def test_is_full(self):
        node = Node(32)
        node.left = Node(100, parent=node)
        node.right = Node(300, parent=node)
        self.assertTrue(node.is_full())

    def test_is_full_is_not_true_when_less_than_two_children_are_present(self):
        node = Node(32)
        node.left = Node(100, parent=node)        
        self.assertFalse(node.is_full())

    def test_is_leaf(self):
        node = Node(32)
        self.assertTrue(node.is_leaf())

    def test_is_leaf_is_not_true_when_children_are_present(self):
        node = Node(32)
        node.left = Node(100, parent=node)
        self.assertFalse(node.is_leaf())

    def test_replace_child(self):
        node = Node(32)
        left = Node(100, parent=node)
        other = Node(44)

        node.left = left
        node.replace_child(node.left, other)

        self.assertEquals(44, node.left.item)
        self.assertIs(node, left.parent)
        self.assertIsNone(other.parent)
