#!/usr/bin/python3
"""
test cases for testing conversion between text node to html node
"""

import unittest
from src.leafnode import LeafNode
from src.textnode import TextNode
from src.to_text import text_node_to_html_node

class ToHTMLNode_Test(unittest.TestCase):
    def test_conversion(self):
        node = LeafNode('a', "Link", {'href': "www.google.com"})
        text_node = TextNode('Link', "link", "www.google.com")
        self.assertEqual(node, text_node_to_html_node(text_node))
        self.assertEqual(node.to_html(), text_node_to_html_node(text_node).to_html())

    def test_italic_conversion(self):
        node = LeafNode('i', "Text", None)
        text_node = TextNode('Text', "italic", None)
        self.assertEqual(node.to_html(), text_node_to_html_node(text_node).to_html())
        self.assertEqual(node, text_node_to_html_node(text_node))

    def test_image_conversion(self):
        node = LeafNode('img', "", {"src": "here", 'alt': "image"})
        text_node = TextNode("image", "image", "here")
        self.assertEqual(node.to_html(), text_node_to_html_node(text_node).to_html())
        self.assertEqual(node, text_node_to_html_node(text_node))

    def test_code_conversion(self):
        node = LeafNode('code', "This is a code to test")
        text_node = TextNode("This is a code to test", "code", None)
        self.assertEqual(node.to_html(), text_node_to_html_node(text_node).to_html())
        self.assertEqual(node, text_node_to_html_node(text_node))

    def test_text_conversion(self):
        node = LeafNode(None, "This is text", None)
        text_node = TextNode("This is text", "text", None)
        self.assertEqual(node.to_html(), text_node_to_html_node(text_node).to_html())
        self.assertEqual(node, text_node_to_html_node(text_node))

    def test_bold_conversion(self):
        node = LeafNode('b', "This is the text", None)
        text_node = TextNode("This is the text", "bold", None)
        self.assertEqual(node.to_html(), text_node_to_html_node(text_node).to_html())
        self.assertEqual(node, text_node_to_html_node(text_node))

if __name__ == '__main__':
    unittest.main()