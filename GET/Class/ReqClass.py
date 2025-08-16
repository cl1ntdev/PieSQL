from fastapi.param_functions import Query


class GetClass:
    def __init__(self):
        self.tableName = ""
        
    #  >> >> >> IMPORTANT << << << # 
    #  Initialize connection first # 
    #  >> >> >> IMPORTANT << << << #     
    
    # Define connection here
    def defineConnection(self,connection):
        self.connection = connection
    
    def checkConnection(self):
        print(self.connection)
    
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
    
    def strChecker(self,value): # To check if the col constraintval (where id = ->[1]<-) is string
        if "-str" in value:
            return True
    
    # =========== # 
    # Read Data #
    # =========== #
    def readData(self,tableName):
        query = "select * from " +  tableName
        print(query)
        
    def readAllDataConst(self,tableName,colConstraint,colConstVal):
        # what if the colCOnstVal is either string or number 
        
        if self.strChecker(colConstVal):
            colConstVal = colConstVal.replace("-str","")
            colConstVal = '"' + colConstVal + '"'
         
        
        query = "Select * from " + tableName + " where " + colConstraint + " = " + colConstVal
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
    