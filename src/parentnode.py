#!/usr/bin/python3
"""
Implementation of the parent node function
"""

from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("The Parent needs tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent should have atleast one children")

        anchor_props = "" if self.props is None else f" {self.props_to_html}"

        child_representation = ""
        for child in self.children:
            """ Inorder traversal to check P L R """
            assert isinstance(child, HTMLNode)
            child_representation += child.to_html()

        return f"<{self.tag}{anchor_props}>{child_representation}</{self.tag}>"

    def __eq__(self, o):
        return super().__eq__(o)
