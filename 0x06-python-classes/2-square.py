#!/usr/bin/python3
# 2-sqaure.py
# Banele Mahlangu <banelemahlangu@gmail.com>
"""Define a class Square."""


class Square:

    """Represnt a new Square.

    Args:
        size (int): The size of the new sqaure.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    self.__size = size