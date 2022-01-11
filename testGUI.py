from tkinter import *




class rootClass(Frame):
    def __init__(self,root):
        super().__init__(root)
        mainFrame = Frame(root,height="500",width="500")
        mainFrame.pack(fill=BOTH,side=TOP,expand=True)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        
        #Menu
        menubar = Menu(root)
        #CourseMenu
        coursemenu = Menu(menubar, tearoff=0,activebackground='yellow green')
        coursemenu.add_command(label="Add Course", command= lambda: self.show_frame("AddCourse"))
        coursemenu.add_command(label="Edit Course", command= lambda: self.show_frame("EditCourse"))
        coursemenu.add_command(label="Delete Course")
        coursemenu.add_separator()
        coursemenu.add_command(label="Exit" ,command=root.quit)
        menubar.add_cascade(label = "Course", menu=coursemenu)
        #ShowMenu
        showmenu = Menu(menubar,tearoff=0,activebackground='yellow green')
        showmenu.add_command(label='All')
        showmenu.add_command(label='Passed')
        showmenu.add_command(label='Not Passed')
        showmenu.add_separator()
        showmenu.add_command(label='Exit', command = root.quit)
        menubar.add_cascade(label='Show Courses', menu = showmenu)
        root.config(menu=menubar)
       
        self.frames = {}
        for F in (AddCourse, EditCourse, DeleteCourse):
            page_name = F.__name__
            frame = F(parent=mainFrame, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AddCourse")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
      











      
#κλαση για την εισαγωγη μαθηματος στην βαση      
class AddCourse(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller 
        self.config(bg="lightblue3") 
        #Labels
        label_course_id = Label(self,text = "Κωδικος Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        label_course_name = Label(self,text = "Ονομα Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        label_course_etc = Label(self,text = "Μοναδες Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        label_course_status = Label(self,text = "Περασμενο/Χρωστουμενο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        label_course_phase = Label(self,text = "Υποχ/ΜΛΟ/ΜΗΥ/ΜΤΔ", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
        label_course_grade = Label(self,text = "Δωσε Βαθμο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")

        #TextField for Labels
        entry_course_id= Entry(self,text="id",font= ('Arial',13))
        entry_course_name= Entry(self,text="name",font= ('Arial',13))
        entry_course_etc= Entry(self,text="etc",font= ('Arial',13))
        entry_course_status= Entry(self,text="status",font= ('Arial',13))
        entry_course_phase= Entry(self,text="phase",font= ('Arial',13))
        entry_course_grade= Entry(self,text="grade",font= ('Arial',13))

        #Buttons
        button_send= Button(self,text="Send",padx=20,pady=10, relief = GROOVE)
        button_clear= Button(self,text="Clear",padx=20,pady=10, relief = GROOVE)

        #Add to Frame 
        #Labels
        label_course_id.grid(row=0 ,column=0,padx=10 , pady=10)
        label_course_name.grid(row=1 ,column=0,padx=10 , pady=10)
        label_course_etc.grid(row=2 ,column=0,padx=10 , pady=10)  
        label_course_status.grid(row=3 ,column=0,padx=10 , pady=10)
        label_course_phase.grid(row=4 ,column=0,padx=10 , pady=10)
        label_course_grade.grid(row=5 ,column=0,padx=10 , pady=10) 
         #TextFields
        entry_course_id.grid(row=0 , column=1,padx=10,pady=10)
        entry_course_name.grid(row=1 , column=1,padx=10,pady=10)
        entry_course_etc.grid(row=2 , column=1,padx=10,pady=10)
        entry_course_status.grid(row=3 , column=1,padx=10,pady=10)
        entry_course_phase.grid(row=4 , column=1,padx=10,pady=10)
        entry_course_grade.grid(row=5 , column=1,padx=10,pady=10)
         #Buttons
        button_send.grid(row =6 , column =0 , padx=10)
        button_clear.grid(row =6 , column =1,padx=10)  
        
        
        
        
        
        
        
        

#Κλαση για την επεξεργασια μαθηματος στην βαση
class EditCourse(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "lightblue3" )
        scrollbar = Scrollbar(self)
        scrollbar.pack(side = RIGHT, fill = Y)
        coursesList = Listbox(self,yscrollcommand= scrollbar.set, bg = "lightblue3" , fg = "goldenrod", selectmode= SINGLE, width=450)
        coursesList.insert(END,"test1")
        coursesList.insert(END,"test2")
        coursesList.pack( side = LEFT , fill = BOTH)
        scrollbar.config(command= coursesList.yview)
        delete = Button(self, text = "Delete")
        delete.pack(side = BOTTOM)

#Κλαση για την διαγραφη μαθηματος απο την βαση
class DeleteCourse(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
         





if __name__ == '__main__':
    root = Tk()
    root.title("Course Project")
    root.iconbitmap("D:\Projects\Python\CoursesProject\icon.ico")
    root.geometry("500x500+700+300")
    
    rootClass(root)
    
    root.mainloop()
    

