#!/usr/bin/python3
"""
The aim of this script is to list all states
whose names start with the letter 'N'
from the database called `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Establish a connection to the database
    and retrieve the states meeting the criteria.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC"
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)
