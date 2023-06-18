#!/usr/bin/python3
""" lists all states with a name starting with N  """

import sys
import MySQLdb

if __name__ = '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection = MySQLdb.connect(host='localhost',
                                 user=username,
                                 port=3306,
                                 passwd=password,
                                 db=db_name)
    curr_obj = connection.cursor()
    curr_obj.execute("SELECT states.id, name FROM states WHERE name "
                     "COLLATE latin1_general_cs "
                     "LIKE 'N%' "
                     "ORDER BY states.id ASC;")
    rows = curr_obj.fetchall()
    for row in rows:
        print(row)

    curr_obj.close()
    connection.close()
