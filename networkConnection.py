#Αρχειο για την διαχειρηση της βασης και των ερωτηματων που θα δημιουργηθουν

import mysql.connector as c
from mysql.connector import Error 
import StudentClass
import cx_Oracle as cx


def OracleConnection():
    connection = cx.connect("it174999/Sg159753!@192.168.6.21:1521/CoursesProject")
    cur = connection.cursor()
    cur.execute('CREATE TABLE Test (PersonID int not null PRIMARY KEY)')
    cur.close()
    connection.close()


#function για την εισαγωγη δεδομενων στον πινακα Student
def dbInsertDataAtStudent(hostname,username,userpass,db,stud):
    try:
        conn=c.connect(host=hostname,user=username,password=userpass,database=db)
        if conn.is_connected:            
            cursor = conn.cursor()
            query = "INSERT INTO Student VALUES (%s,%s,%s)"
            data=(stud.name,stud.lname,stud.id)
            cursor.execute(query,data)
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

            


#st=StudentClass.Student("kostas","konstantinidhs",174998)
#dbInsertDataAtStudent("localhost","admin","Sg147896325!","CoursesPROJECT",st)
OracleConnection()



