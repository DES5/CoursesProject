""" Κλαση για την συνδεση με την βαση 
    dbname -> Ονομα της βασης 
    dbtable-> ονομα του πινακα τησ βασης 
    username -> Ονομα του χρηστη
    userpass -> Κωδικος του χρηστη
    dbtype -> Τυπος βασης
"""
import mysql.connector as c
from mysql.connector import Error 



    
''' try:
    self.conn =c.connect(host=self.dbtype,user=self.username,password=self.userpass,database=self.dbname)
    if self.conn.is_connected:
        print ("Succeful Connection with " + self.dbname)
        print("Version: " + self.conn.get_server_info())
except Error as e:
    print("Error while try connecting with server ", e) '''


#funtion για την αποσυνδεση με την βαση
''' def dbDisconnect(self):
try:
    if self.conn.is_connected:    
        self.conn.close()
        print("Succeful Disconnect from " + self.dbname)
except Error as e:
    print("Error while try to disconnect from server", e) 
 '''


#function για την εισαγωγη δεδομενων στον πινακα Student
def dbInsertDataAtStudent(hostname,username,userpass,db):
    try:
        conn=c.connect(host=hostname,user=username,password=userpass,database=db)
        if conn.is_connected:
            query = """INSERT INTO ExampleTable 
                    VALUES ('hi',29)"""
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("The Table has updated")
    except Error as e:
        print("Fail with updated the table: {}".format(e))
        conn.rollback()
    finally:
        if conn.is_connected:
            cursor.close()
            conn.close()
            print("Succeful disconect from server")

            



dbInsertDataAtStudent("localhost","admin","Sg147896325!","Example")



