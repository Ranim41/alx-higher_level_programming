#!/usr/bin/python3
"""
toka
"""

def read_file(filename=""):
    """
    tooka
    """
    
    with open(filename, 'r', encoding="utf-8") as f:
        read_content = f.read()
        print(read_content, end='')