#!/usr/bin/env python3
"""
Here is my block implemnetation
"""


from src.textnode import TextNode
from src.htmlnode import ParentNode
from src.splitter import *
from src.to_text import *
from functools import reduce


def markdown_to_html_node(markdown):
    mkd_list = markdown_to_blocks(markdown)
    childrens = [block_to_html(block) for block in mkd_list]

    return ParentNode('div', childrens)

def markdown_to_blocks(markdown):
    return markdown.split('\n\n')


def block_to_block_type(markdown_block):
    mkd_is_block_mapping = {
        "heading": lambda mkd_block: mkd_block.startswith('#') and mkd_block.lstrip('#') != '' and mkd_block.lstrip('#')[0] == ' ',
        "code": lambda mkd_block: mkd_block.startswith('```') and mkd_block.endswith('```'),
        "quote": lambda mkd_block: mkd_block.startswith('> '),
        "unordered_list": is_unordered_list,
        "ordered_list": is_ordered_list
    }

    for block, is_block in mkd_is_block_mapping.items():
        if is_block(markdown_block):
            return block
    
    return "paragraph"


def block_to_html(markdown_block):
    block_type = block_to_block_type(markdown_block)
    
    if block_type in ['ordered_list', 'unordered_list']:
        return get_list_node(markdown_block, block_type)

    return get_html_block(markdown_block, block_type)



def get_list_node(markdown_block, block_type):
    regex = r'^\d+\. '
    list_tag = 'ol'
    if block_type is 'unordered_list':
        list_tag = 'ul'
        regex = r'- ' if markdown_block.startswith('-') else r'\* '

    print("----")
    print(markdown_block)
    childrens = list(map(
        lambda cur_list: ParentNode(
            'li', block_content_to_html_childrens(re.split(regex, cur_list)[1])
            ), markdown_block.split('\n')
    ))

    return ParentNode(list_tag, childrens)


def get_html_block(markdown_block, block_type):
    block_type_to_htmlnode = {
        "heading": lambda mkd_block: ParentNode(
            f'h{(len(mkd_block) - len(mkd_block.lstrip("#")))}', block_content_to_html_childrens(mkd_block.lstrip('#'))
            ),
        "code": lambda mkd_block: ParentNode('pre', [LeafNode('code', mkd_block.strip('```'))]),
        "quote": lambda mkd_block: LeafNode('blockquote', mkd_block.replace('> ', ''))
        }

    if block_type in block_type_to_htmlnode.keys():
        return block_type_to_htmlnode[block_type](markdown_block)
    
    return ParentNode('p', block_content_to_html_childrens(markdown_block))

def block_content_to_html_childrens(text):

    text_nodes = text_to_textnodes(text)
    childrens = [text_node_to_html_node(node) for node in text_nodes]

    return childrens


def is_unordered_list(markdown_block: str):
    if len(markdown_block.split('\n')) == 1:
        return markdown_block.startswith('* ') or markdown_block.startswith('- ')

    return reduce(
        lambda a, b: a and is_unordered_list(b),
        markdown_block.split('\n'),
        True
        )


def is_ordered_list(markdown_block: str) -> bool:
    return reduce(
        lambda a, b: a and b[1].strip(' ').startswith(f"{b[0] + 1}."),
        enumerate(markdown_block.split('\n')),
        True
        )
