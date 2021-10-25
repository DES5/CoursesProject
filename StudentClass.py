#Η κλαση Student 
#name -> Ονομα φοιτητη 
#fname -> Επιθετο φοιτητη
#id -> Ο ακαδημαικος Κωδικος του φοιτητη 

from random import randint


class Student:
    def __init__(self,name,fname):
        self.name=name
        self.fname=fname
        self.id=name[0].lower() + fname[0].lower() + str(randint(100, 999))
        


       

