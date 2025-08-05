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
        
def GetAllDataConst(conn,tableName,constraint):
    # constraint must start from "where"
    try:
        query = "Select * from " + tableName + " " + constraint
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
    except Error as e:
        print("error is + ",e)
    
    