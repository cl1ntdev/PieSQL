class GetTableData():
    def __init__(self,tableName,dataValue,constraint):
        self.tableName = tableName
        
    def getAllQuery(self):
        return "select * from " + self.tableName
