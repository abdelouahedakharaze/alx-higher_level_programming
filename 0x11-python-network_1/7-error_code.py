#!/usr/bin/python3
"""Accepts a URL as input, sends a request to
 that URL, and then displays the body of the response."""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
