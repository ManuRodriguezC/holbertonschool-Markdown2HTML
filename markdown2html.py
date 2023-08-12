#!/usr/bin/python3
"""
Convert markdown to html
This file read readme.md and write in readme.html
"""
import sys
import os
import markdown

# Checks if it receives less than two arguments
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check id the input file exist
if not os.path.isfile(input_file):
    sys.stderr.write(f"Missing {input_file}")
    sys.exit(1)

# Open the input file and read the information
with open(input_file, "r") as mdfile:
    content = mdfile.read()
    html_content = markdown.markdown(content)

# Open the putput file and write information in html
with open(output_file, "w") as html_file:
    html_file.write(html_content)

sys.exit(0)
