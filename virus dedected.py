#Import nessasary libraries
from tkinter import*
from tkinter import messagebox
#setup tkinter window
root=Tk()
root.geometry("100*100")
#function Display warning messafe
#This will be called one the button is clicked
#messagebox.showwarning("window Name",text to be displayed")
def msg():
    messagebox.showwarning("Alert","Stop!Virus to be found")
#Adding Button widget to window
button=Button(root,text="Scan for virus",command=msg)
#Entering main event loop
root.mainloop()