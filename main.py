#Εφαρμογη που δειχνει τα περασμενα μαθηματα με χρηση GUI και παιρνει τα δεδομενα απο μια βαση Δεδομενων που ειναι ανεβασμενη localhost/phpadmin 


from tkinter import * 
import StudentClass as StudentC


#Κυριως προγραμμα 


def main():
    root = Tk() #the main wigtet 
    titleLabel = Label(root, text= "Εφαρμογη εμφανισεις των μαθηματων")
    titleLabel.pack()


    root.mainloop()


main()





