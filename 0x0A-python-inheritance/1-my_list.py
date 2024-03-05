#!/usr/bin/python3
"""Defines a subclass Mylist inherited from superclass list"""


class MyList(list):
    """Subclass inherited from superclass list"""

    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
