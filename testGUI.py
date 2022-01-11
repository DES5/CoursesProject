from tkinter import *




class rootClass(Label):
    def __init__(self,root):
        super().__init__(root)
        self.mainFrame = Frame(root,height="500",width="500",bg='lightblue3')
        self.mainFrame.pack(fill=BOTH,side=TOP,expand=True)
        #Menu
        self.menubar = Menu(root)
        #CourseMenu
        self.coursemenu = Menu(self.menubar, tearoff=0,activebackground='yellow green')
        self.coursemenu.add_command(label="Add Course")
        self.coursemenu.add_command(label="Edit Course")
        self.coursemenu.add_command(label="Delete Course")
        self.coursemenu.add_separator()
        self.coursemenu.add_command(label="Exit" ,command=root.quit)
        self.menubar.add_cascade(label = "Course", menu=self.coursemenu)
        #ShowMenu
        self.showmenu = Menu(self.menubar,tearoff=0)
        
        
        
        
        
        
        
        
         


        #Labels
        self.label_course_id = Label(self.mainFrame,text = "Κωδικος Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_name = Label(self.mainFrame,text = "Ονομα Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_etc = Label(self.mainFrame,text = "Μοναδες Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_status = Label(self.mainFrame,text = "Περασμενο/Χρωστουμενο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_phase = Label(self.mainFrame,text = "Υποχ/ΜΛΟ/ΜΗΥ/ΜΤΔ", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        self.label_course_grade = Label(self.mainFrame,text = "Δωσε Βαθμο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")

        #TextField for Labels
        self.entry_course_id= Entry(self.mainFrame,text="id",font= ('Arial',13))
        self.entry_course_name= Entry(self.mainFrame,text="name",font= ('Arial',13))
        self.entry_course_etc= Entry(self.mainFrame,text="etc",font= ('Arial',13))
        self.entry_course_status= Entry(self.mainFrame,text="status",font= ('Arial',13))
        self.entry_course_phase= Entry(self.mainFrame,text="phase",font= ('Arial',13))
        self.entry_course_grade= Entry(self.mainFrame,text="grade",font= ('Arial',13))

        #Buttons
        self.button_send= Button(self.mainFrame,text="Send",padx=20,pady=10, relief = GROOVE)
        self.button_clear= Button(self.mainFrame,text="Clear",padx=20,pady=10, relief = GROOVE)

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

        root.config(menu=self.menubar)



        


























if __name__ == '__main__':
    root = Tk()
    root.title("Course Project")
    root.iconbitmap("D:\Projects\Python\CoursesProject\icon.ico")
    root.geometry("500x500+700+300")
    
    rootClass(root)
    root.mainloop()


