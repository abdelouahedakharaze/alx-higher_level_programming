#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Determine if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to compare the object's type to.

    Returns:
        True if obj is an instance or inherited instance of a_class,or False.
    """

    if isinstance(obj, a_class):
        return True
    return False
