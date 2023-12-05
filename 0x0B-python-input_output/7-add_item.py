#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    sj = __import__("7-save_to_json_file").save_to_json_file
    lj = __import__("8-load_from_json_file").load_from_json_file

    try:
        items = lj("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    sj(items, "add_item.json")
