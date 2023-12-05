#!/usr/bin/python3

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Provide a list of attributes accessible for an object."""
    return dir(obj)
