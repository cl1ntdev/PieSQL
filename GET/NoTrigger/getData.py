from mysql.connector import Error
from connector.DbConnection import app,defaultConnection

@app.get("/getData")
def GetAllData(table):
    query = "Select * from words"
  
    try:
        connection = defaultConnection()
        if not connection:
            return{"error":"connection getData failed"}
            
            
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return {"data": result}
    except Error as e:
        print("Error is ",e)
    