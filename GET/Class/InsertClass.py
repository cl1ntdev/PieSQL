class InsertDataTable():
    def __init__(self):
        self.tableName = ""
        
    def defineSelf(self,tableName,arrValues):
        self.tableName = tableName
        self.arrValues = arrValues
    
    def addValues(self,arrValues):
        self.arrValues = arrValues
        
    def insertData(self):   
        return "the total number of array is ", len(self.arrValues) 