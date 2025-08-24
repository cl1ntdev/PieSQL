import mysql.connector
from mysql.connector import Connect, Error, MySQLConnection
from fastapi import FastAPI
from connector.GlobalHost import MainHost
from typing import Optional

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
    user = 'root'
    passwd = 'clinT'
    db = "pyweirdool"
    port =3306
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = db
        )
    
    except Error as e:
        print("Error found: ",e)
    return connection

# Need to pass in values for connection
