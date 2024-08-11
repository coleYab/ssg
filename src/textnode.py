#!/usr/bin/python3
"""
TextNode: representation of a text element.
"""

class TextNode:
    """
    TextNode: main node for the text.
    """
    def __init__(self, text, text_type, url=None):
        """
        __init__: main constructor that will identify the properties of the
                 inline text secton.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, o):
        return (
                self.text == o.text and
                self.text_type == o.text_type and
                o.url == self.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
