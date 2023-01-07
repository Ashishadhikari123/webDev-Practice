#!/bin/python3

# script to create readme
import os

HEADER = """# webdev cookbook\n
"""

BODY = ""

FOOTER = """\n---\n
Made by Ashish Adikhari, Shivanshu
"""

CWD = os.getcwd()
LENGTH = len(CWD)

def generate_body(dir, space=0):
    global BODY
    SPACE = " " * space
    items = os.listdir(dir)
    for item in items:
        if item == ".git":
            continue
        citem = os.path.join(dir, item)
        if citem == dir:
            continue
        elif os.path.isfile(citem):
            if citem.endswith(".html"):
                BODY += SPACE + "- [" + item + "]" + "(" + citem[LENGTH:] + ")\n"
        else:
            BODY += SPACE + "- " + item + "\n"
            generate_body(citem, space + 4)

generate_body(os.getcwd())

# open file
f = open("README.md", "w+", encoding="utf-8")
f.write(HEADER)
f.write(BODY)
f.write(FOOTER)
