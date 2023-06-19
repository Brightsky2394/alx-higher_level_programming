#!/usr/bin/python3
"""
script that takes in arguments and
displays all values in the states table.
It's safe from MySQL injection!
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name)
    curr = conn.cursor()

    query = """
    SELECT states.id, name FROM states WHERE name = %s
    COLLATE latin1_general_cs
    ORDER BY states.id ASC;
    """

    curr.execute(query, (state_name, ))

    rows = curr.fetchall()
    for row in rows:
        print(row)
