#!/usr/bin/python3
'''A script to list out all the components of the
'hbtn_06_0_usa' database
'''
import MySQLdb
import sys


def select_states(username, passwd, db_name):
    '''contains the code that handles listing of the contents of the database
    '''
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=passwd,
            db=db_name,
            port=3306)
    cur = db.cursor()  # Creating a cursor object
    sql = """
    SELECT cities.id, cities.name, states.name
    FROM cities LEFT JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.commit()
    cur.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    select_states(username, passwd, db_name)  # Call the function
