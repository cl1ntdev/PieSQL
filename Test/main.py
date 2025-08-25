import os 
from ast import Delete
from copy import Error
from connector.DbConnection import createConnection,defaultConnection
from GET.Class.ReqClass import GetClass
from rich.console import Console 
def clrscrn():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

host = '127.0.0.1'
username = 'root'
password = 'clinT'
db = "pyweirdool"
port =3306

def main():
   clrscrn()
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

    print(">> Read DATA <<               >> INSERT DATA <<")
    print("[1] Specific Data             [3] Specific Data")
    print("[2] All Data")
    print(">> UPDATE DATA <<             >> DELETE DATA << ")
    print("[5]. Specific Data            [6] Specific Data ")
    print("\n")
    print("[7] Exit Program ")
    
    ch = int(input("Choice: "))
    print("\n")
    
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
                tableName = "words"
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
            case 8:
                clrscrn()


















main();
