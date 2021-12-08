#Αρχειο για την διαχειρηση της βασης και των ερωτηματων που θα δημιουργηθουν

import psycopg2 as p
import StudentClass
from configparser import ConfigParser



def config(filename='database.ini',section='postgres'):
    parser = ConfigParser()
    parser.read(filename)
    db={}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    else:
        raise Exception ("Section {0} not found in the {1} file".format(section,filename))
    return db


def PostgresStartConn():
    conn=None
    try:
        params=config()
        print("Connecting")
        conn = p.connect(**params)
    except (Exception, p.Error) as error:
        print(error)
    finally:
        return conn
    


def PostgresStopConn():
    try:
        conn=PostgresStartConn()
    except:
        raise Exception("Never establish connection!")
    finally:
        conn.close()
        
        














































# def PostGresConnevtion():
#     cx.connect("it174999/Sg159753!@1
#     connection = c.connect(host=)
#     cur = connection.cursor()
#     cur.execute('CREATE TABLE Test (PersonID int not null PRIMARY KEY)')
#     cur.close()
#     connection.close()



#function για την εισαγωγη δεδομενων στον πινακα Student
# def dbInsertDataAtStudent(hostname,username,userpass,db,stud):
#     try:
#         conn=c.connect(host=hostname,user=username,password=userpass,database=db)
#         if conn.is_connected:            
#             cursor = conn.cursor()
#             query = "INSERT INTO Student VALUES (%s,%s,%s)"
#             data=(stud.name,stud.lname,stud.id)
#             cursor.execute(query,data)
#             conn.commit()
#             print("The Table has updated")
#     except Error as e:
#         print("Fail with updated the table: {}".format(e))
#         conn.rollback()
#     finally:
#         if conn.is_connected:
#             cursor.close()
#             conn.close()
#             print("Succeful disconect from server")

            


#st=StudentClass.Student("kostas","konstantinidhs",174998)
#dbInsertDataAtStudent("localhost","postgres","159753@","CoursesProject",st)
PostgresStartConn()



