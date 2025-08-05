from mysql.connector import Error

def changeData(conn,tableName,value):
    try:
        query = ""
    except Error as e:
        print("Error in postData.py",e)