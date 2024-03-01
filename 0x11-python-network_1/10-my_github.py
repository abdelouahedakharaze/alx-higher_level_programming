#!/usr/bin/python3

"""
This function takes GitHub credentials as
input and utilizes the GitHub API to retrieve and
display the user's ID.
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
