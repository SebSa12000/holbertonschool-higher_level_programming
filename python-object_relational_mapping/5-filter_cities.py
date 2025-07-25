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
    cur.execute("SELECT cities.name "
                "FROM states "
                "INNER JOIN cities ON cities.state_id = states.id  "
                "WHERE states.name = %s"
                "ORDER BY cities.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join((city[0]) for city in query_rows))
    cur.close()
    db.close()
