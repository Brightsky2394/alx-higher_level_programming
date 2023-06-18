#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    curr_obj = db.cursor()
    curr_obj.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in curr_obj.fetchall() if state[1][0] == "N"]i
