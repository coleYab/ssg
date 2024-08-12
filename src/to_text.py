#!/usr/bin/python3

from src.leafnode import LeafNode
from src.htmlnode import HTMLNode
from src.parentnode import ParentNode
from src.textnode import TextNode

def text_node_to_html_node(text_node: TextNode):
    """
    functoin to convert text node to a html node.
    """
    text_type = {
        "text": text_type_text,
        "bold": text_type_bold,
        "italic": text_type_italic,
        "code": text_type_code,
        "link": text_type_link,
        "image": text_type_image 
        }
    
    if text_node.text_type not in text_type.keys():
        raise KeyError(f"<{text_node.text_type}> is not valid text.")

    return text_type[text_node.text_type](text_node) 
    
def text_type_text(text_node):
    return LeafNode(None, text_node.text)

def text_type_italic(text_node):
    return LeafNode('i', text_node.text)

def text_type_bold(text_node):
    return LeafNode('b', text_node.text)

def text_type_code(text_node):
    return LeafNode('code', text_node.text)

def text_type_link(text_node):
    return LeafNode('a', text_node.text, {'href': text_node.url})

def text_type_image(text_node):
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

