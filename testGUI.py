from tkinter import *




class rootClass(Label):
    def __init__(self,root):
        super().__init__(root)
        self.insertCourseFrame = Frame(root,height="500",width="500",bg='lightblue3')
        self.menuFrame = Frame(root,height=80,width="500", bg ='red')
        self.menuFrame.pack(side = TOP,expand=True,fill=BOTH)
        self.insertCourseFrame.pack(fill=BOTH,side=TOP,expand=True)

        #Labels
        self.label_course_id = Label(self.insertCourseFrame,text = "Κωδικος Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_name = Label(self.insertCourseFrame,text = "Ονομα Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_etc = Label(self.insertCourseFrame,text = "Μοναδες Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_status = Label(self.insertCourseFrame,text = "Περασμενο/Χρωστουμενο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_phase = Label(self.insertCourseFrame,text = "Υποχ/ΜΛΟ/ΜΗΥ/ΜΤΔ", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_grade = Label(self.insertCourseFrame,text = "Δωσε Βαθμο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")

        #TextField for Labels
        self.entry_course_id= Entry(self.insertCourseFrame,text="id",font= ('Arial',13))
        self.entry_course_name= Entry(self.insertCourseFrame,text="name",font= ('Arial',13))
        self.entry_course_etc= Entry(self.insertCourseFrame,text="etc",font= ('Arial',13))
        self.entry_course_status= Entry(self.insertCourseFrame,text="status",font= ('Arial',13))
        self.entry_course_phase= Entry(self.insertCourseFrame,text="phase",font= ('Arial',13))
        self.entry_course_grade= Entry(self.insertCourseFrame,text="grade",font= ('Arial',13))

        #Buttons
        self.button_send= Button(self.insertCourseFrame,text="Send",padx=20,pady=10, relief = GROOVE)
        self.button_clear= Button(self.insertCourseFrame,text="Clear",padx=20,pady=10, relief = GROOVE)

        #Add to Frame 
        #Labels
        self.label_course_id.grid(row=0 ,column=0,padx=10 , pady=10)
        self.label_course_name.grid(row=1 ,column=0,padx=10 , pady=10)
        self.label_course_etc.grid(row=2 ,column=0,padx=10 , pady=10)  
        self.label_course_status.grid(row=3 ,column=0,padx=10 , pady=10)
        self.label_course_phase.grid(row=4 ,column=0,padx=10 , pady=10)
        self.label_course_grade.grid(row=5 ,column=0,padx=10 , pady=10) 
         #TextFields
        self.entry_course_id.grid(row=0 , column=1,padx=10,pady=10)
        self.entry_course_name.grid(row=1 , column=1,padx=10,pady=10)
        self.entry_course_etc.grid(row=2 , column=1,padx=10,pady=10)
        self.entry_course_status.grid(row=3 , column=1,padx=10,pady=10)
        self.entry_course_phase.grid(row=4 , column=1,padx=10,pady=10)
        self.entry_course_grade.grid(row=5 , column=1,padx=10,pady=10)
         #Buttons
        self.button_send.grid(row =6 , column =0 , padx=10)
        self.button_clear.grid(row =6 , column =1,padx=10)
































if __name__ == '__main__':
    root = Tk()
    root.title("Course Project")
    root.iconbitmap("D:\Projects\Python\CoursesProject\icon.ico")
    root.geometry("500x500+700+300")
    
    rootClass(root)
    root.mainloop()


