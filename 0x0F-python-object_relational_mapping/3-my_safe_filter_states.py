#!/usr/bin/python3
""" import and print database MySQL """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )
    curr = conn.cursor()
    curr.execute(
        "SELECT * FROM states where name=%s ORDER BY states.id", (argv[4], )
        )
    for i in cur.fetchall():
        print(i)
    curr.close()
    conn.close()
