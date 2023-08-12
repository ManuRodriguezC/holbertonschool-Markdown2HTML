#!/usr/bin/python3
"""
Convert markdown to html
This file read readme.md and write in readme.html
"""
import sys
import markdown


def markdown_to_html(md_file, output_file):
    """
    Check the argv of the sys and the files in the path
    """
    try:
        with open(md_file, "r") as file:
            markdown_cont = file.read()
        html_cont = markdown.markdown(markdown_cont)

        with open(output_file, "w") as file:
            file.write(html_cont)

    except FileNotFoundError:
        sys.stderr.write(f"Missing {md_file}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    md_file = sys.argv[1]
    output_file = sys.argv[2]

    markdown_to_html(md_file, output_file)
