#jessica hall
#06/25/24
#csd210


import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # establishing connection
        connection = mysql.connector.connect(
            host='localhost',         #'localhost'
            database='movies', # db
            user='root',     #'root'
            password='0910'  #password
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version", db_info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connected to database:", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_mysql()
