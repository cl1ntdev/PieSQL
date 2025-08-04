from mysql.connector import Error
from connector.DbConnection import app
from connector.DbConnection import defaultConnection


@app.get("/getData")
def GetAllData():
    tableName = "words"
    query = "Select * from " + tableName
    connection = None
    try:
        connection = defaultConnection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return {"data": result}
    except Error as e:
        print("Error is ",e)
    