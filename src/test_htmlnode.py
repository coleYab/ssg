#!/usr/bin/python3
"""
TestCases for htmlnode
"""

from src.htmlnode import HTMLNode
import unittest

class HTMLNodeTest(unittest.TestCase):
    def test_props_for_a(self):
        html_node = HTMLNode('a', "TestIT", None, {'href': 'https://google.com'})
        self.assertEqual(html_node.props_to_html(), 'href="https://google.com"')
    
    def test_to_props_returns_none(self):
        html_node = HTMLNode('a', "TestIT", None, None)
        self.assertEqual(html_node.props_to_html(), None)    

    def test_to_props_with_two_props(self):
        html_node = HTMLNode('a', "TestIT", None, {'href': 'www.test', 'style': 'test'})
        self.assertEqual(html_node.props_to_html(), 'href="www.test" style="test"')

    def test_props_with_three_props(self):
        html_node = HTMLNode('a', "TestIT", None, {'href': 'www.test', 'style': 'test', 'wtf': 'nothing'})
        self.assertEqual(html_node.props_to_html(), 'href="www.test" style="test" wtf="nothing"')


if __name__ == '__main__':
    unittest.main()
