#!/usr/bin/python3
'''select states'''


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
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM states "
                "INNER JOIN cities ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
