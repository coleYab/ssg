#!/usr/bin/python3
"""
HTMLNode class to represent in the entire assignment
"""

from functools import reduce

class HTMLNode:
    def __init__(self, tag, value, children, props):
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

        return ''

    def __re__(self):
        return f"HTMLNode => tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

    def __eq__(self, o):
        return (
            self.tag == o.tag and
            self.value == o.value and
            self.children == o.children and
            self.props == o.props
        )
