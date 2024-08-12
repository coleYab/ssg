#!/usr/bin/python3

import unittest
from src.splitter import *
from src.textnode import TextNode

class SplitterTest(unittest.TestCase):
    def test1(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ])

    def test_with_unfinished(self):
        node = TextNode("This is a text with `non complete code block", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [node])

    def test_with_nomarkup(self):
        node = TextNode("This is a text with no code block", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [node])
