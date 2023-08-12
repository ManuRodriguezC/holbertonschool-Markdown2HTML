#!/usr/bin/python3
'''
This module check the files params in the sys

Argv[1] is a file input
Argv[2] is a file output
'''
import sys
import os


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)
    
    with open(input_file, "r") as file_input:
        html = []
        for i in file_input:
            if i.startswith('#'):
                list_tag = i.split()
                num = list_tag[0].count('#')
                string = f"<h{num}>"
                count = 0
                for run in list_tag:
                    if count > 0 and count != 1:
                        string += " "
                        string += list_tag[count]
                    if count == 1:
                        string += list_tag[count]
                    count += 1
                string += f"</h{num}>\n"
                html.append(string)
    
    with open(output_file, "w") as file_output:
        for dates in html:
            file_output.write(dates)
    
    
    sys.exit(0)
