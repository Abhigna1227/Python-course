#import nessasary libraries
from tkinter import *
#create window
window=Tk()
window.title("Event Handler")
window.geometry=(100*100)
#bind key press to handle_ketpress()
window.bind("<Key>")
#Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")
button=Button(text="click me!please!")
button.pack()
#Blind click event to handle check
button.bind("<Button-1>",handle_click)
window.mainloop()
     