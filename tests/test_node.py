"""
Contains unit tests for verifying correctness of Node-related algorithms.
"""
from unittest import TestCase

from evored.tree import Node


class NodeTest(TestCase):
    """
    Test suite for Node.
    """

    def test_choose_child_returns_none_when_no_children_are_present(self):
        node = Node(32)
        self.assertIs(None, node.choose_child())

    def test_choose_child_returns_left_when_only_left_is_present(self):
        node = Node(32)
        node.left = Node(42, parent=node)
        self.assertIs(node.left, node.choose_child())

    def test_choose_child_returns_right_when_only_right_is_present(self):
        node = Node(32)
        node.right = Node(42, parent=node)
        self.assertIs(node.right, node.choose_child())
    
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

        self.assertEquals(other, node.left)
        self.assertIs(node, left.parent)
        self.assertIsNone(other.parent)

    def test_swap_children(self):
        node = Node(32)
        left = Node(12, parent=node)
        right = Node(42, parent=node)

        node.left = left
        node.right = right
        node.swap_children()

        self.assertIs(right, node.left)
        self.assertIs(left, node.right)

    def test_swap_places_with_same_parent(self):
        node = Node(32)
        left = Node(42, parent=node)
        right = Node(52, parent=node)

        node.left = left
        node.right = right
        left.swap_places(right)

        self.assertIs(right, node.left)
        self.assertIs(left, node.right)
