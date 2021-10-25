""" Η κλαση Course
    Name -> Το ονομα του μαθηματος str
    ID -> Ο κωδικος του μαθηματος (πρωτευων) str
    Phase -> Αμα το μαθημα ειναι Υποχρεωτικο (Υ) Μηχανικου Λογισμηκου (ΜΛΟ) Μηχανικος Ηλεκτ Υπολογιστων (ΜΗΥ) Τεχνικος Δικτυων (ΜΤΔ) str
    Status -> Η φαση του μαθηματος δλδ αμα ειναι περασμενο (Π) η χρωστουμενο (Χ) str
    Etc -> Η μοναδες το καθε μαθηματος int
    Grade -> Ο βαθμος του μαθηματος int """


class Course:
    def __init__(self,name,id,phase,status,etc,grade):
        self.name=name
        self.id=id
        self.phase=phase
        self.status=status
        self.etc=etc
        self.grade=grade

        