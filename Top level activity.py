#Import necessary libraries
from tkinter import *
#setting up main window
root=Tk()
root.geometry("400x300")
root.title("main")
#Function to open new top level window
def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("top.level")
    l2=Label(top,text="This is top level window")
    l2.pack()
    top.mainloop()
l=Label(root,text="This is a root window")
btn=Button(root,text="Click me to see magic",command=topwin)
l.pack()
btn.pack()
