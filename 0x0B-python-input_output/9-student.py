#!/usr/bin/python3
"""
tooka
"""


class Student:
    """
    class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        tooka
        """
        return self.__dict__.copy()
