from mysql.connector import Error

def changeData(conn,tableName,value,valueTo):
    try:
        query = "set " + value + " to " + valueTo 
    except Error as e:
        print("Error in postData.py",e)