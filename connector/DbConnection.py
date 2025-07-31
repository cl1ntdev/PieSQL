import mysql.connector
from mysql.connector import Connect, Error

def createConnection(host,username,password,db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            username = username,
            passwd = password,
            database = db
        )
    
    except Error as e:
        print("Error found: ",e)
    return connection

# Need to pass in values for connection
