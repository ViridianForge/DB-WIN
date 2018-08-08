#Python to test connection to CW Mysql Database

import mysql.connector
from mysql.connector import errorcode

config = {
    'user':'root',
    'password':'Ch1p7un35',
    'host':'127.0.0.1',
    'database':'chipwin_db'
}

try:
    cnx = mysql.connector.connect(**config)
    #Buffered so we can use a second cursor
    cursor = cnx.cursor(buffered=True)
    cursor.execute('SHOW tables;')
    for (table_name,) in cursor:
        print(table_name)
        print('Description of Table:')
        sub_cursor = cnx.cursor()
        print('test 1')
        sub_cursor.execute('DESCRIBE album;')
        print('test 2')
        queryRows = sub_cursor.fetchall()
        for row in queryRows:
            print(row)
            print('\n')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
