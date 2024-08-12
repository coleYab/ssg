#!/usr/bin/python3
"""
Some tests for the leaf nodes including some edge cases
"""

import unittest
from src.leafnode import LeafNode

class LeafNodeTest(unittest.TestCase):
    def test_leaf_anchor_html(self):
        node = LeafNode('a', 'Its Link', {'href': 'https://google.com'})
        expected_html = '<a href="https://google.com">Its Link</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_with_none_value(self):
        self.assertRaisesRegex(ValueError, "All leaf nodes must have a value", lambda: LeafNode('a', None, {}))

if __name__ == '__main__':
    unittest.main()