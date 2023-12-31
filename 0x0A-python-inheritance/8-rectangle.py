#!/usr/bin/python3
""" a generic documentation to test checker"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

""" a generic documentation to test checker"""


class Rectangle(BaseGeometry):
    """Define a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
