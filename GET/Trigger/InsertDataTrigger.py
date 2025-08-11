from mysql.connector import Error 

def InsertData(conn,query):
    try:
        connection = conn
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        connection.close()
    except Error as e:
        print("error InsertDataTrigger: ",e)