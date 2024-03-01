#!/usr/bin/python3
"""Accepts a URL as input, sends a request to that URL, and
displays the body of the response."""
if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
