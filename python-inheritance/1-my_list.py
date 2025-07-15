#!/usr/bin/python3
"""
Module: 1-my_list
Defines a class MyList that inherits from list
and prints the list in sorted order without modifying the original.
"""

class MyList(list):
    """A subclass of list with a method to print sorted list."""

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))