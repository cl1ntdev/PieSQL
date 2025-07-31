from copy import Error
from connector.DbConnection import createConnection

host = '127.0.0.1'
username = 'root'
password = 'clinT'
db = "pyweirdool"
port =3306

def main():
    try:
        connection = createConnection(host,username,password,db)
        if connection:
            print("suceessfully connected")
        else: 
            print("error")
    except Error as e:
        print(e)    
        
        
main();