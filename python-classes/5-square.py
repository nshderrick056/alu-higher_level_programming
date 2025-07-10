#!/usr/bin/python3
"""Defines a class Square that can print itself with '#' characters."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize square using the setter for validation."""
        self.size = size

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
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
