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
   isEnd = False
   title = """
    ██████╗░██╗███████╗░██████╗░██████╗░██╗░░░░░
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██║░░░░░
    ██████╔╝██║█████╗░░╚█████╗░██║██╗██║██║░░░░░
    ██╔═══╝░██║██╔══╝░░░╚═══██╗╚██████╔╝██║░░░░░
    ██║░░░░░██║███████╗██████╔╝░╚═██╔═╝░███████╗
    ╚═╝░░░░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝
    by - clint
    """
   
   
   while not isEnd:
    print(title)
# Crud
    print(">> Read DATA <<")
    print("1. Specific Data") # done
    print("2. All Data") # done
    
    print(">> INSERT DATA << ")
    print("3. Specific Data")
    
    print(">> UPDATE DATA << ")
    print("5. Specific Data")
    
    print(">> DELETE DATA << ")
    print("6. Specific Data")
    print("7: Exit ")
    
    
    ch = int(input("Choice: "))
    
    match ch:
            case 1:
                dbConnection = defaultConnection()
                tableName = "word"
                colConst = "id"
                colConstVal = "1-str"
                data = GetClass()
                data.defineConnection(defaultConnection)
                data.checkConnection()
                data.readAllDataConst(tableName,colConst,colConstVal)
            case 2:
                print("Choice is "+ str(ch) +" result is: ")
                tableName = "word"
                data = GetClass()
                data.readData(tableName)
                print(data)
            case 3:
                tableName = "food"
                valuesToInsert = ["macaron","1-str","nice"] # pass in the values here any valus
                columnNames = ["column1","column2","column3"] # pass the column to with they are assigned
                insert = GetClass()
            
                insert.insertData(tableName,columnNames,valuesToInsert)
            case 5:
                table = "food"
                col1 = "sweet"
                col1Val = "candy-str"
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
            case 7:
                isEnd = True


















# main();
