#!/usr/bin/python3
"""
LeafNode - the implementation for the node in the html dom that has no child
"""

from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        """
        Constructor: that takes tag, value of that tag and its property
        """
        if value is None:
            raise ValueError('All leaf nodes must have a value')
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        html_props = "" if self.props is None else f" {self.props_to_html()}"
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

    def __eq__(self, o):
        return super().__eq__(o)
