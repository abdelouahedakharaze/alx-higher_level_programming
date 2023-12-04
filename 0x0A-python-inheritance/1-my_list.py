#!/usr/bin/python3


class MyList(list):
    """Realizes sorted printing functionality for the standard list class."""

    def print_sorted(self):
        """Display a list in ascending sorted order."""
        print(sorted(self))
