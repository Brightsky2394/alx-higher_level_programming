#!/usr/bin/python3
"""
lists all states with a name starting with N
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                 passwd=argv[2], db=argv[3])

    curr_obj = db.cursor()
    curr_obj.execute("SELECT * FROM states \
                      WHERE name LIKE BINARY 'N%' \
                      ORDER BY states.id ASC")
    rows = curr_obj.fetchall()

    for row in rows:
        print(row)
curr_obj.close()
connection.close()
