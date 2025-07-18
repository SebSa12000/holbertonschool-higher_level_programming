#!/usr/bin/python3
'''Import of states'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
        )
    cur = db.cursor()
    value = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
