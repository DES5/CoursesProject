""" Η κλαση Course
    Name -> Το ονομα του μαθηματος str
    ID -> Ο κωδικος του μαθηματος (πρωτευων) str
    Phase -> Αμα το μαθημα ειναι Υποχρεωτικο (Υ) Μηχανικου Λογισμηκου (ΜΛΟ) Μηχανικος Ηλεκτ Υπολογιστων (ΜΗΥ) Τεχνικος Δικτυων (ΜΤΔ) str
    Status -> Η φαση του μαθηματος δλδ αμα ειναι περασμενο (Π) η χρωστουμενο (Χ) str
    Etc -> Η μοναδες το καθε μαθηματος int
    Grade -> Ο βαθμος του μαθηματος int """


class Course:
    
    __etc=6
    
    def __init__(self,name,id,phase,status,grade):
        self.__name=name
        self.__id=id
        self.__phase=phase
        self.__status=status
        self.__grade=grade

    @property
    def name(self):
        return self.__name  
    
    @property
    def id(self):
        return self.__id
    
    
    @property
    def phase(self):
        return self.__phase
    
    
    @property
    def status(self):
        return self.__status
    
    
    @property
    def grade(self):
        return self.__grade
    
    @property
    def etc(self):
        return self.__etc
    
    @name.setter
    def name(self,name):
        self.__name=name
    
    @id.setter
    def id(self,id):
        self.__id=id
    
    @phase.setter
    def phase(self,phase):
        self.__phase=phase
    
    @status.setter
    def status(self,status):
        self.__status=status
    
    @grade.setter
    def grade(self,grade):
        self.__grade=grade
    
    
    