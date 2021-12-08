from tkinter import *


root = Tk()
#new = Tk()

def aaa():
   new = Tk() 
   label1=Label(new,text="test").pack()

label1=Label(root,text="test").pack()
myButton=Button(root,text="Click Me!",command=aaa).pack()

# myLabel=Label(root,text="Hello")
# mylabel2=Label(root,text="My name is Stefanos")
# myButton=Button(root,text="Click Me!", state=DISABLED,padx=50,pady=50,command=test)

# myButton.config(state=NORMAL)


# e = Entry(root,font=("Arrial"))


# myLabel.grid(row=0,column=1)
# mylabel2.grid(row=1,column=0)







root.mainloop()