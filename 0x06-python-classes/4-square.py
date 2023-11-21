#!/usr/bin/python3
# 4-square.py
"""Define a class Square following Google-style docstrings."""


class Square:
    """This class represents a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a new Square.
        area(self): Return the current area of the square.

    Properties:
        size: Get/set the current size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
