import mysql.connector
from mysql.connector import Connect, Error
from fastapi import FastAPI
from connector.GlobalHost import MainHost

app = FastAPI()


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

# This is the global host alternative, define variables here
def defaultConnection():
    host = '127.0.0.1'
    username = 'root'
    password = 'clinT'
    db = "pyweirdool"
    port =3306
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
