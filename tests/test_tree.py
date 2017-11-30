"""
Contains unit tests for verifying correctness of Tree-related algorithms.
"""
from unittest import TestCase

import itertools

from evored.tree import Tree


class TreeTest(TestCase):
    """
    Test suite for Tree.
    """

    def test_build(self):
        tree = Tree([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(1, tree.root.item)
        self.assertEqual(2, tree.root.left.item)
        self.assertEqual(3, tree.root.right.item)
        self.assertEqual(4, tree.root.left.left.item)
        self.assertEqual(5, tree.root.left.right.item)
        self.assertEqual(6, tree.root.right.left.item)
        self.assertEqual(7, tree.root.right.right.item)

    def test_build_with_moderate_numbers_of_elements(self):
        items = list(range(0, 1000))
        tree = Tree(items)
        for node, item in itertools.zip_longest(tree, items):
            self.assertEqual(item, node.item)

    def test_choose_node_returns_none_when_tree_is_empty(self):
        tree = Tree()
        self.assertIs(None, tree.choose_node())

    def test_choose_node_returns_root_when_only_root_is_present(self):
        tree = Tree([1])
        self.assertIs(tree.root, tree.choose_node())
