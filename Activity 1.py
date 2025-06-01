from tkinter import *
root=Tk()
root.title('number pad')
root.geometry('250x300')
num=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    root.coloumnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    for i in range(4):
        for j in range(3):
            frame=Frame(master=root,
                        relif=SUNKEN,
                        borderwidth=1,
                        bg=("#6b599a"))
            frame.grid(row=i,coloumn=j,sticky="nsew")
            label=label(master=frame,text=num[i][j],bg="#287196",font=('Arial',18))
            label.pack(expand=True,fill='both,padx=5,paddy=5')
root.mainloop()
