#!/usr/bin/python3
"""
This is Document
"""
import sys
import os
# import markdown

def convert_markdown_to_html(markdown_filename, output_filename):
    """
    Converts Markdown content from the specified file to HTML and writes it to the output file.

    Args:
        markdown_filename (str): Path to the Markdown input file.
        output_filename (str): Path to the HTML output file.

    Raises:
        FileNotFoundError: If the specified Markdown file doesn't exist.

    Returns:
        None
    """
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
        print(f"Usage: ./markdown2html.py {sys.argv[1]} {sys.argv[2]}", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.exists(input_filename):
        print(f"Missing {input_filename}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_filename, output_filename)
    sys.exit(0)
