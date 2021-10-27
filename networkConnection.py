""" Κλαση για την συνδεση με την βαση 
    dbname -> Ονομα της βασης 
    dbtable-> ονομα του πινακα τησ βασης 
    username -> Ονομα του χρηστη
    userpass -> Κωδικος του χρηστη
    dbtype -> Τυπος βασης
"""
import mysql.connector as c

class networkConnection:

    def __init__(self,dbname,username,userpass,dbtype):
        self.dbname=dbname
        self.username=username
        self.userpass=userpass
        self.dbtype=dbtype
        try:
            self.conn =c.connect(host=self.dbtype,user=self.username,password=self.userpass,database=self.dbname)
            if self.conn.is_connected:
                print(self.conn.connection_id)
                print ("Succeful Connection with " + self.dbname)
        except ConnectionError as erro:
            print(erro)


    #funtion για την αποσυνδεση με την βαση
    def dbDisconnect(self):
        try:
            if self.conn.is_connected:    
                self.conn.close()
                print("Succeful Disconnect from " + self.dbname)
        except ConnectionError as erro:
            print(erro) 

            
test=networkConnection("Example","admin","Sg147896325!","localhost")
test.dbDisconnect()


