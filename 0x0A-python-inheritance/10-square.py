#!/usr/bin/python3
""" a generic documentation to test checker"""
Rectangle = __import__("9-rectangle").Rectangle

""" a generic documentation to test checker"""


class Square(Rectangle):
    """Define a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
