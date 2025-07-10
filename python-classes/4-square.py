#!/usr/bin/python3
"""Defines a class Square with controlled access to size."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize square and set size via setter for validation."""
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Retrieve the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
