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
    
    #  >> >> >> << << <<  # 
    #   Data Manipulation # 
    #  >> >> >> << << <<  #     
    
    def strChecker(self,value): # To check if the col constraintval (where id = ->[1]<-) is string
        if "-str" in value:
            value = value.replace("-str","")
            value = '"' + value + '"'
            return value
        else:
            return value
    
    # =========== # 
    # Read Data #
    # =========== #
    def readData(self,tableName):
        query = "select * from " +  tableName
        print(query)
        
    def readAllDataConst(self,tableName,colConstraint,colConstVal):
       
       colConstVal = self.strChecker(colConstVal) # returns a value stringified ( 1-str -> "1" ) 
       query = "Select * from " + tableName + " where " + colConstraint + " = " + colConstVal
       print(query)
        
           
           
           
    # =========== # 
    # Insert Data #
    # =========== # 
    def insertData(self,tableName,colNames,valInsert):  
        # insert into tableName(?) values (?)
        modifiedValInsert = []
        
        for i in range(len(valInsert)): # column size is equal to values size or number of values to be inserted
            print(valInsert[i])
            modifiedValInsert.append(self.strChecker(valInsert[i]))
    
        query = "insert into " + tableName + "(" + ",".join(colNames) + ")" + " values(" + ",".join(modifiedValInsert) + ")"
        # map the column where values to be added 
        
        print(query) 
        
        
        
        
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
    