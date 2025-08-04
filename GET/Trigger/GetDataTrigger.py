from mysql.connector import Error
from connector.DbConnection import app

def GetAllData(conn,tableName):
    query = "Select * from " + tableName
    connection = None
    try:
        connection = conn
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return {"data": result}
    except Error as e:
        print("Error is ",e)
    