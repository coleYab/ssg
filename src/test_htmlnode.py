#!/usr/bin/python3
"""
TestCases for htmlnode
"""

from src.htmlnode import HTMLNode
import unittest

class HTMLNodeTest(unittest.TestCase):
    def test_props_for_a(self):
        html_node = HTMLNode('a', "TestIT", None, {'href': 'https://google.com'})


if __name__ == '__main__':
    unittest.main()
