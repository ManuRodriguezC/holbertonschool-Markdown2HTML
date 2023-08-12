#!/usr/bin/python3
import sys
import os
import markdown

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    sys.stderr.write(f"Missing {input_file}")
    sys.exit(1)

with open(input_file, "r") as mdfile:
    content = mdfile.read()
    html_content = markdown.markdown(content)

with open(output_file, "w") as html_file:
    html_file.write(html_content)
    

sys.exit(0)