#Η κλαση Student 
#name -> Ονομα φοιτητη 
#fname -> Επιθετο φοιτητη
#id -> Ο ακαδημαικος Κωδικος του φοιτητη 

from random import randint


class Student:

    def __init__(self,name,lname,id):
        self.__name=name
        self.__lname=lname
        self.__id=id
        
        
    @property
    def name(self):
        return self.__name
    
    @property
    def lname(self):
        return self.__lname
    
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self,name):
         self.__name=name 
         
    @lname.setter
    def lname(self,lname):
        self.__lname=lname
    
    @id.setter
    def id(self,id):
        self.__id=id
        
        
        
    
    
        
  

