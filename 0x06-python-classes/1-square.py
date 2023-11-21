#!/usr/bin/python3
# 1-square.py
"""Define a class Square following Google-style docstrings."""


class Square:
    """This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initialize a new Square.

    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
