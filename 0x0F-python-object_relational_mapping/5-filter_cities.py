#!/usr/bin/python3
'''A script to list out all the components of the
'hbtn_06_0_usa' database
'''
import MySQLdb
import sys


def select_states(username, passwd, db_name, state_name):
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
    SELECT cities.name
    FROM cities LEFT JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE BINARY '{}'
    ORDER BY cities.id ASC;
    """.format(state_name)
    cur.execute(sql)
    rows = cur.fetchall()
    # prints out the values of the data returned from the database
    for num_row, row in enumerate(rows):
        print(row[0], end="")
        if num_row < (len(rows) - 1):
            print(", ", end="")
    print()
    db.commit()
    cur.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = (sys.argv[4].split('; '))[0].strip("'").strip('"')
    select_states(username, passwd, db_name, state_name)  # Call the function
