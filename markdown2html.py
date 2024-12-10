#!/usr/bin/python3
"""
Markdown to HTML converter
"""

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    with open(markdown_file, 'r') as md, open(html_file, 'w') as html:
        for line in md:
            html.write(line)
    exit(0)
