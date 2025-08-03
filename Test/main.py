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
   ch = input("Choice: ")
   
   match ch:
       case 1:
          try:
              print("Choice is "+ ch +" result is: ")
              data = GetAllData(defaultConnection(),"words")
          except Error as e:
              print("Error is",e)
         
           
       
       
       
       
       
       
       
       

        
main();