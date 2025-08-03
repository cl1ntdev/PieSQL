from copy import Error
from connector.DbConnection import createConnection,defaultConnection
from GET.GetData import GetAllData


host = '127.0.0.1'
username = 'root'
password = 'clinT'
db = "pyweirdool"
port =3306

def main():
   print("1. Get all Data")
   ch = int(input("Choice: "))
   
   match ch:
       case 1:
            print("Choice is "+ str(ch) +" result is: ")
            data = GetAllData(defaultConnection(),"words") # pass in the connection and the table name 
            print(data)
         
           
       
       
       
       
       
       
       
       

        
main();