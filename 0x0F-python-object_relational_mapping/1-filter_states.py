#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curr_obj = connection.cursor()
    curr_obj.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in curr_obj.fetchall() if state[1][0] == "N"]
