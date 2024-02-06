#!/usr/bin/python3
"""
toooka
"""
import json


def load_from_json_file(filename):
    """
    toooka
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
