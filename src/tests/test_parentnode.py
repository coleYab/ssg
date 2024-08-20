#!/usr/bin/python3
"""
testing parent node
"""

from src.htmlnode import LeafNode, ParentNode
import unittest

class ParentNodeTest(unittest.TestCase):
    def test_leaf_node_raises(self):
        node1 = ParentNode(None, None, None)
        self.assertRaisesRegex(ValueError, "The Parent needs tag", lambda: node1.to_html())

    def test_no_child(self):
        node2 = ParentNode('a', None, None)
        self.assertRaisesRegex(ValueError, "Parent should have atleast one children", lambda: node2.to_html())

    def test_to_html(self):
        node = ParentNode('p',     [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ], None)
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_with_nested_parents(self):
        node = ParentNode('p', [
            ParentNode('a', [
                LeafNode('button', "Its Button")
            ]),
            LeafNode('a', 'Link')
            ], None)
        expected_html = '<p><a><button>Its Button</button></a><a>Link</a></p>'
        self.assertEqual(node.to_html(), expected_html)
