#!/usr/bin/python3
""" List all states """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection = MySQLdb.connector(host='localhost', port=3306,
                                   user=username, db=db_name, passwd=password)
    curr_obj = connection.cursor()
    curr_obj.execute(SELECT states.id, name FROM states ORDER BY states.id ASC)
    rows = curr_obj.fetchall()
    for row in rows:
        print(row)

    curr_obj.close()
    connection.close()
