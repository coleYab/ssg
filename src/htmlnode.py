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
            return reduce(
                lambda x, y: f"{x} {conv_props(y)}",
                self.props.items(), ""
                ).strip()

        return None
