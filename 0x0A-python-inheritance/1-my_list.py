#!/usr/bin/python3
"""Defines a class-checking function."""


class MyList(list):
    """Realizes sorted printing functionality for the standard list class."""

    def print_sorted(self):
        """Display a list in ascending sorted order."""
        print(sorted(self))
