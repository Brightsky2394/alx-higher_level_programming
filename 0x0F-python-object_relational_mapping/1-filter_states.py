#!/usr/bin/python3
""" Filter states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name)
    curr_obj = conn.cursor()
    curr_obj.execute("SELECT states.id, name FROM states WHERE name "
                     "COLLATE latin1_general_cs "
                     "LIKE 'N%' "
                     "ORDER BY states.id ASC;")
    rows = curr_obj.fetchall()
    for row in rows:
        print(row)

    curr_obj.close()
    conn.close()
