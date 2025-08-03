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
   print("1. Get Data")
   # Get specific Data
   # Get all Data 
   print("2. Insert Data")
   # insert specific Data
   # insert all Data
   print("3. Update Data")
   # update specific Data
   # update all Data
   print("1. Delet all Data")
   # delete specific Data
   # delete all Data
   
   ch = int(input("Choice: "))
   
   match ch:
       case 1:
            print("Choice is "+ str(ch) +" result is: ")
            data = GetAllData(defaultConnection(),"words") # pass in the connection and the table name 
            print(data)
         
           
       
       
       
       
       
       
       
       

        
main();