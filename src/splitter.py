#!/usr/bin/python3
"""
Splitter: the function to split the tasks
"""

from src.textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

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
        
        next_idx = text.find(delimiter, idx + 1)
        if next_idx == -1:
            res.append(old_node)
            return

        res.append(TextNode(text[:idx], old_node.text_type))
        res.append(TextNode(text[idx+1:next_idx], text_type))
        find_all_res(TextNode(text[next_idx + 1:], old_node.text_type))
        return

    for node in old_nodes:
        find_all_res(node)
    
    return res
