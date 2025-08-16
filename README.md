Goal: Backend Setup for future projects

## TODO

7. <> Query indentification passing int or string
8. Integrate db modification inside class so it wont be on a separate file 
9. restructure and clean file before proceeding

# NOTES
-! Classes are still used to make query statements 

## Folders

> connector.dbConnection has function
 - createConnection // manual make connection for different database connections
 - defaultConnection // used for a single database

> GET.NoTigger.getData
 - start server: uvicorn GET.NoTrigger.getData:app --reload
 - uses [app] from connector.dbConnection focused only on getting data
 - has default table value // open for testing

> POST.POSTData
 - uses [app] from connector.dbConnection focused only on post data


# Functions
  > GetAllDataConst(connection,tablename,constraint)
  tableName = String
  constraint = String (ex "where a like b")
  
  > GetAllData(connection,tablename)
  - get all data, tableName = string
  
  > changeData(conn,tableName,value,valueTo)
  - param conn = connection from sql, table name, first value, to change value


## HOW TO USE 
> Parameters in ReqClass
 - tableName: Table Name of a database 
 - _upColName: Column Name to update its value
 - _upColValue: Column Name to value use for update
 - colConstraint: Column Constratint (where ->[id]<- = 1)
 - colConstVal : Column value of the constraint (where id = ->[1]<-)

> Passing Integer or String in params 
 - use "-str" to indicate that the value is a string else dont use anythhing if ur passing an int