#!/usr/bin/python3
"""
Splitter: the function to split the tasks
"""

import typing
from src.textnode import TextNode
from src.regex_taxes import *


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def text_to_textnodes(text):
    res = []
    text_type_mapping = {
        '`': text_type_code,
        '**': text_type_bold,
        '*': text_type_italic
    }
    res = split_nodes_delimiter([TextNode(text, text_type_text)], '`', text_type_code)

    for delimeter, text_type in text_type_mapping.items():
        res = split_nodes_delimiter(res, delimeter, text_type)

    res = split_nodes_image(res)
    res = split_nodes_link(res)

    return res


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    splitting every node delimiter.
    """
    res = []

    def find_all_res(old_node):
        nonlocal res, delimiter, text_type
        text = old_node.text

        idx = text.find(delimiter)
        if idx == -1:
            res.append(old_node)
            return
        
        next_idx = text.find(delimiter, idx + len(delimiter))
        if next_idx == -1:
            res.append(old_node)
            return

        res.append(TextNode(text[:idx], old_node.text_type))
        res.append(TextNode(text[idx+len(delimiter):next_idx], text_type))
        find_all_res(TextNode(text[next_idx + len(delimiter):], old_node.text_type))
        return

    for node in old_nodes:
        find_all_res(node)
    
    return list(filter(lambda node: len(node.text) != 0, res))


def split_nodes_image(old_nodes: typing.List[TextNode]):
    res = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            res.append(node)
            continue

        text_nodes = re.split(r'!\[[^\]]*\]\([^)]*\)', node.text)
        for i in range(len(text_nodes)):
            if len(text_nodes[i].strip()) != 0:
                res.append(TextNode(text_nodes[i], node.text_type, node.url))

            if i != len(text_nodes) - 1:
                res.append(TextNode(images[i][0], text_type_image, images[i][1]))

    return res


def split_nodes_link(old_nodes: typing.List[TextNode]):
    res = []

    for node in old_nodes:

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            res.append(node)
            continue

        text_nodes = re.split(r'\[[^\]]*\]\([^)]*\)', node.text)
        for i in range(len(text_nodes)):
            if len(text_nodes[i].strip()) != 0:
                res.append(TextNode(text_nodes[i], node.text_type, node.url))
            
            if i != len(text_nodes) - 1:
                res.append(TextNode(links[i][0], text_type_link, links[i][1]))

    return res
