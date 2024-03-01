#!/usr/bin/python3
"""Accepts a URL as input, sends a request
to that URL, and then displays the value of the variable
'X-Request-Id' in the response header."""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
