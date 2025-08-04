class GetTableData():
    def __init__(self,tableName,constraint):
        self.tableName = tableName
        
    def getAllQuery(self):
        return "select * from " + self.tableName