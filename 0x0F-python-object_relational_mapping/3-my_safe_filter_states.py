#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    curr_obj = conn.cursor()
    curr_obj.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    [print(states) for states in curr_obj.fetchall()]
