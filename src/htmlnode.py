#!/usr/bin/python3
"""
HTMLNode class to represent in the entire assignment
"""

from functools import reduce

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Under construction")

    def props_to_html(self):
        conv_props = lambda x: f'{x[0]}="{x[1]}"'
        if isinstance(self.props, dict):
            return " " + reduce(
                lambda x, y: f"{x} {conv_props(y)}",
                self.props.items(), ""
                ).strip()

        return ''

    def __repr__(self):
        return f"HTMLNode => tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

    def __eq__(self, o):
        return (
            self.tag == o.tag and
            self.value == o.value and
            self.children == o.children and
            self.props == o.props
        )


class LeafNode(HTMLNode):
    """
    LeafNode - a node that inherits form HTML Node.
    """
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
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, o):
        return super().__eq__(o)


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
