from fastapi.param_functions import Query


class GetClass:
    def __init__(self):
        self.tableName = ""
        
    def addTableName(self,tableName):
        self.tableName =  tableName
    
    def addValues(self, valuesToInsert):
        self.valInsert =  valuesToInsert
      
    def addColNames(self,colNames):
        self.colNames =  colNames
        
    def getAllQuery(self):
        return "select * from " + self.tableName
    
    def defineSelf(self,tableName,valuesToInsert,colNames):
        self.tableName = tableName
        self.valInsert = valuesToInsert
        self.colNames = colNames
       
       # Use for updating
    def addUpdateVal(self,_upColName,_upColValue,colConstraint,colConstVal):
        self.upColName = _upColName
        self.upColValue = _upColValue
        self.colConstraint = colConstraint
        self.colConstVal = colConstVal
    # =========== # 
    # Read Data #
    # =========== #
    def readData(self,tableName):
        query = "select * from " +  tableName
        print(query)
           
    # =========== # 
    # Insert Data #
    # =========== # 
    def insertData(self):  
        
        numIndicator = "-int"
        query = "insert into " + self.tableName
        
        # map the column where values to be added 
        qCols = "(" + ",".join(self.colNames) + ")"
        query+=qCols
        # map the column where values to be added 
        colVal =" values(" + ",".join(self.valInsert) + ")"
        query+=colVal
        
        return query 
        
    # =========== # 
    # Update Data #
    # =========== #
    
    def updateData(self,tableName,_upColName,_upColValue,colConstraint,colConstVal):
        query2 = "update " + tableName + " set " + _upColName + "= "  + _upColValue + " where " + colConstraint + "= " + colConstVal
        
        print (query2)
    # =========== # 
    # Delte Data #
    # =========== #
    def deleteData(self,tableName,colConstraint,colConstVal):
        query2 = "delete from " + tableName + " where " + colConstraint + "= " + colConstVal
        
        print (query2)
    