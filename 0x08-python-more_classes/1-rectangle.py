#!/usr/bin/python3
""" A class Rectangle """


class Rectangle:
    """ Initialize rectangle attributes """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """ Width getter """
        return self._width

    @width.setter
    def width(self, value):
        """ Width setter """
        self._width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Height getter """
        return self._height

    @height.setter
    def height(self, value):
        """ Height setter """
        self._height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
