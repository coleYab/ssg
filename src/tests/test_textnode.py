import unittest

from src.textnode import TextNode

class TextNodeTest(unittest.TestCase):
    """
    TextNodeTest: testing the textnode class.
    """

    def test_eq(self):
        node1 = TextNode("This is a bold text", "bold")
        node2 = TextNode("This is a bold text", "bold")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a link", "a", "/users")
        node2 = TextNode("This is a link", "a", "/persons")
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node2.url, None)

if __name__ == "__main__":
    unittest.main()
