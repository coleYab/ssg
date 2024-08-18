#!/usr/bin/python3
"""
tasks that are done with regexes
"""
import re

def extract_markdown_images(text):
    regex = r'!\[([^\]]*)\]\(([^)]*)\)'

    pattern = re.findall(regex, text)

    return pattern

def extract_markdown_links(text):
    regex = r'[^!]\[([^\]]*)\]\(([^)]*)\)'

    pattern = re.findall(regex, text)

    return pattern
