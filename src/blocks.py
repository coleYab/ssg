#!/usr/bin/env python3
"""
Here is my block implemnetation
"""

from functools import reduce

class BlockType:
    def __init__(self, text, tag) -> None:
        self.text = text
        self.tag = tag

def markdown_to_blocks(markdown):
    return list(map(lambda block: block.strip(), markdown.split('\n\n')))

def block_to_block_type(markdown_block):
    pass

def is_code_block(markdown_block: str):
    if markdown_block.startswith('```') and markdown_block.endswith('```'):
        return True
    return False

def is_headings(markdown_block: str):
    return markdown_block.startswith('#')

def is_unordered_list(markdown_block: str):
    if len(markdown_block.split('\n')) == 1:
        return markdown_block.startswith('*') or markdown_block.startswith('-')

    return reduce(
        lambda a, b: a and is_unordered_list(b),
        markdown_block.split('\n'),
        True
        )

def is_ordered_list(markdown_block: str) -> bool:
    return reduce(
        lambda a, b: a and b[1].startswith(f"{b[0] + 1}."),
        enumerate(markdown_block.split('\n')),
        True
        )
