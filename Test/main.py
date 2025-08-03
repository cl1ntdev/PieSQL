from copy import Error
from connector.DbConnection import createConnection,defaultConnection
from GET.GetData import GetAllData


host = '127.0.0.1'
username = 'root'
password = 'clinT'
db = "pyweirdool"
port =3306

def main():
# Crud
   print("GET DATA")
   print("1. Specific Data")
   print("2. All Data")
   
   print("INSERT DATA")
   print("3. Specific Data")
   print("4. Get All Data")
   
   print("UPDATE DATA")
   print("5. Specific Data")
   print("6. All Data")
   
   print("DELETE DATA")
   print("7. Specific Data")
   print("8. All Data")
   
   
   ch = int(input("Choice: "))
   
   match ch:
       case 1:
            print("Choice is "+ str(ch) +" result is: ")
            data = GetAllData(defaultConnection(),"words") # pass in the connection and the table name 
            print(data)
         
           
       
       
       
       
       
       
       
       

        
main();