from ast import Delete
from copy import Error
from connector.DbConnection import createConnection,defaultConnection
from GET.Class.ReqClass import GetClass

host = '127.0.0.1'
username = 'root'
password = 'clinT'
db = "pyweirdool"
port =3306

def main():
# Crud
   print("GET DATA")
   print("1. Specific Data") # done
   print("2. All Data") # done
   
   print("INSERT DATA")
   print("3. Specific Data")
   print("4. All Data")
   
   print("UPDATE DATA")
   print("5. Specific Data")
   
   print("DELETE DATA")
   print("6. Specific Data")
   
   
   ch = int(input("Choice: "))
   
   match ch:
        case 1:
            
            print("test")
            tableName = "word"
            constraint = "where id = 1"
            data = GetClass()
            data.readAllDataConst(tableName,constraint)
        case 2:
            print("Choice is "+ str(ch) +" result is: ")
            tableName = "word"
            data = GetClass()
            data.readData(tableName)
            print(data)
        case 3:
            tableName = "food"
            valuesToInsert = ["macaron","1-int","nice"] # pass in the values here any valus
            columnNames = ["column1","column2","column3"] # pass the column to with they are assigned 
            insert = GetClass()
            insert.addTableName(tableName)
            insert.addValues(valuesToInsert)
            insert.addColNames(columnNames)
            insert.insertData()
        case 5: 
            table = "food"
            col1 = "sweet"
            col1Val = "candy"
            colConstraint = "ID"
            colConstraintVal = "1"
            update = GetClass()
            update.updateData(table,col1,col1Val,colConstraint,colConstraintVal)
        case 6: 
            table = "word"
            colConstraint = "id"
            colConstraintVal = "1"
            delete = GetClass()
            delete.deleteData(table,colConstraint,colConstraintVal)
            
            
            
            
            
            
            
           
       
       
       
       
       
       
       
       

        
main();