Goal: Backend Setup for future projects

## TODO
1. Basic CRUD and functions for data modification
3. <> Create class for CRUD of a table
4. Create post to change data ?
5. Insert Data

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
