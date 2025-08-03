from fastapi import FastAPI
from mysql.connector import Error

def GetAll(conn,tableName):
    query = "Select * from " + tableName
    connection = None
    try:
        connection = conn
        
    except Error as e:
        print("Error is ",e)
    