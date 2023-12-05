#!/usr/bin/python3
""" a generic documentation to test checker"""


class MyInt(int):
    """Reverse the integer operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
