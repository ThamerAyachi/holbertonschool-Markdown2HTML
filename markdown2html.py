#!/usr/bin/python3

import sys
import os
# import markdown

def convert_markdown_to_html(markdown_filename, output_filename):
    try:
        with open(markdown_filename, 'r', encoding='utf-8') as markdown_file:
            markdown_text = markdown_file.read()
            # html_text = markdown.markdown(markdown_text)

            with open(output_filename, 'w', encoding='utf-8') as html_file:
                html_file.write(markdown_text)
    except FileNotFoundError:
        print(f"Missing {markdown_filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.exists(input_filename):
        print(f"Missing {input_filename}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_filename, output_filename)
    sys.exit(0)
