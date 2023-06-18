#!/usr/bin/python3
""" Filter states by user input """

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
    curr_obj = conn.cursor()

    query = """
    SELECT states.id, name FROM states WHERE name='{:s}'
    COLLATE latin1_general_cs
    ORDER BY states.id ASC;
    """.format(state_name)

    curr_obj.execute(query)
    rows = curr_obj.fetchall()
    for row in rows:
        print(row)

    curr_obj.close()
    conn.close()
