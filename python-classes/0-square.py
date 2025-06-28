#!/usr/bin/python3
"""Module that defines a Square class."""

class Square:
    """Class that defines a square by its size."""
    def __init__(self, size):
        """Initialize the square with a private size attribute.

        Args:
            size: The size of the square (no type/value validation yet).
        """
        self.__size = size
