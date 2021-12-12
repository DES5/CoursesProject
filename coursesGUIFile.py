from tkinter import *

#TO DO να βαλω τιτλο στο insertCourseFarame να φτιαξο το μενου και επισης να κανω δυναμικο το insertCourseFrame 

root = Tk()
root.title("Ελεγχος Μαθηματων")
root.iconbitmap("D:\Projects\Python\CoursesProject\icon.ico")
root.geometry("500x500+700+300")


#Variables
height = 500
width = 500
menu_color = "#232F347"
body_color = "#4A6572" 


#Δημιουργια Frame
insertCourseFrame = Frame(root,height=height,width=width,bg='lightblue3')
menuFrame = Frame(root,height=80,width=width, bg ='red')
menuFrame.pack(side = TOP,expand=True,fill=BOTH)
insertCourseFrame.pack(fill=BOTH,side=TOP,expand=True)


#Labels
label_course_id = Label(insertCourseFrame,text = "Κωδικος Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
label_course_name = Label(insertCourseFrame,text = "Ονομα Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
label_course_etc = Label(insertCourseFrame,text = "Μοναδες Μαθηματος", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
label_course_status = Label(insertCourseFrame,text = "Περασμενο/Χρωστουμενο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
label_course_phase = Label(insertCourseFrame,text = "Υποχ/ΜΛΟ/ΜΗΥ/ΜΤΔ", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")
label_course_grade = Label(insertCourseFrame,text = "Δωσε Βαθμο", font = ('Arial',13,'bold'),padx=5,pady=5,bg="lightblue3",fg="goldenrod")

#TextField for Labels
entry_course_id= Entry(insertCourseFrame,text="id",font= ('Arial',13))
entry_course_name= Entry(insertCourseFrame,text="name",font= ('Arial',13))
entry_course_etc= Entry(insertCourseFrame,text="etc",font= ('Arial',13))
entry_course_status= Entry(insertCourseFrame,text="status",font= ('Arial',13))
entry_course_phase= Entry(insertCourseFrame,text="phase",font= ('Arial',13))
entry_course_grade= Entry(insertCourseFrame,text="grade",font= ('Arial',13))

#Buttons 
button_send= Button(insertCourseFrame,text="Send",padx=20,pady=10, relief = GROOVE)
button_clear= Button(insertCourseFrame,text="Clear",padx=20,pady=10, relief = GROOVE)

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



root.mainloop()















