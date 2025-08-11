class InsertDataTable():
    def __init__(self):
        self.tableName = ""
        
    def defineSelf(self,tableName,valuesToInsert,colNames):
        self.tableName = tableName
        self.valInsert = valuesToInsert
        self.colNames = colNames
        
    def addValues(self,arrValues):
        self.arrValues = arrValues
        
    def insertData(self):   
        return "the total number of array is ", len(self.arrValues) 