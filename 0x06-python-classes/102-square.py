#!/usr/bin/python3
# 102-square.py
"""Define a class Square following Google-style docstrings."""


class Square:
    """This class represents a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a new Square.
        area(self): Return the current area of the square.

    Comparisons:
        __eq__(self, other): Define the == comparison to a Square.
        __ne__(self, other): Define the != comparison to a Square.
        __lt__(self, other): Define the < comparison to a Square.
        __le__(self, other): Define the <= comparison to a Square.
        __gt__(self, other): Define the > comparison to a Square.
        __ge__(self, other): Define the >= comparison to a Square.

    Properties:
        size: Get/set the current size of the square.

    Raises:
        TypeError: If size is not an integer or if the other object in
        comparisons is not a Square.

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

    def __eq__(self, other):
        """Define the == comparision to a Square.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the areas are equal, False otherwise.

        Raises:
            TypeError: If the other object is not a Square.
        """
        if not isinstance(other, Square):
            raise TypeError("Can only compare with another Square")
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        Raises:
            TypeError: If the other object is not a Square.
        """
        if not isinstance(other, Square):
            raise TypeError("Can only compare with another Square")
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is less than the other, False otherwise.

        Raises:
            TypeError: If the other object is not a Square.
        """
        if not isinstance(other, Square):
            raise TypeError("Can only compare with another Square")
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is less than or equal to the other,
            False otherwise.

        Raises:
            TypeError: If the other object is not a Square.
        """
        if not isinstance(other, Square):
            raise TypeError("Can only compare with another Square")
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is greater than the other, False otherwise.

        Raises:
            TypeError: If the other object is not a Square.
        """
        if not isinstance(other, Square):
            raise TypeError("Can only compare with another Square")
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is greater than or equal to the other,
            False otherwise.

        Raises:
            TypeError: If the other object is not a Square.
        """
        if not isinstance(other, Square):
            raise TypeError("Can only compare with another Square")
        return self.area() >= other.area()
