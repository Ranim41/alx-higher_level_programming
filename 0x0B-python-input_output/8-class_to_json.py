#!/usr/bin/python3
"""
atooka
"""


def class_to_json(obj):
    """
    atooka
    """

    ranim = {}
    if hasattr(obj, "__dict__"):
        ranim = obj.__dict__.copy()
    return ranim
