#!/usr/bin/python3


def is_inherited_instance(obj, target_class):
    """Checks if an object is an inherited instance of a specific class.

    Args:
        obj (any): The object to be checked.
        target_class (type): The class to compare the object's type to.

    Returns:
        True if obj is an inherited instance of target_class, otherwise False.
    """
    return isinstance(obj, target_class) and type(obj) is not target_class
