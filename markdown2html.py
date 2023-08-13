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

    with open(output_file, "w") as out:
        with open(input_file, "r") as int:
            datas = int.readlines()
            for i in range(len(datas)):
                if datas[i].startswith("#"):
                    num = datas[i].count("#")
                    text = datas[i].replace("#", "")[1:]
                    text = text.replace("\n", "")
                    string = f"<h{num}>{text}</h{num}>\n"
                    out.write(string)

                if datas[i].startswith("-"):
                    if datas[i][0] == "-" and datas[i-1][0] != "-":
                        string = "<ul>\n"
                        out.write(string)
                    text = datas[i].replace("- ", "")
                    text = text.replace("\n", "")
                    string = f"<li>{text}</li>\n"
                    out.write(string)
                    if i + 1 < len(datas) and datas[i + 1][0] != "-":
                        string = "</ul>\n"
                        out.write(string)
                    if i + 1 == len(datas):
                        string = "</ul>\n"
                        out.write(string)

    sys.exit(0)
