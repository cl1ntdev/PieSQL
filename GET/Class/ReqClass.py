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
        
    # insert Data
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