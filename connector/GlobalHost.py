
  
class Host:
    def __init__(self,host,username,password,db):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        
        
host = '127.0.0.1'
username = 'root'
password = 'clinT'
db = "pyweirdool"
port =3306

MainHost = Host(host,username,password,db)