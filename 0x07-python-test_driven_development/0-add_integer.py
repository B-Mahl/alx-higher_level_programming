#!/usr/bin/python3
"""Defines an integer addition funtion"""

def add_integer(a, b=98):
    """Retrun the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a ot b is non-interger and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
