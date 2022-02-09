from tkinter import *

colorPalet={'back':'#19282F','front':'#B33030'}

#-------window configuration -----------
win=Tk() 
win.geometry("500x500")
win.resizable(False,False)
win.title("TO DO")
win.config(bg=colorPalet['back'])
#--------------------main manipulations
class Task:
    def __init__(self,parent,content):
        self.f=Frame(parent)
        self.f.pack(pady=2)
        self.label=Label(self.f,text=content,width=50)
        self.label.pack(side="left")
        self.butotn=Button(self.f,text="delete",command=self.delett)
        self.butotn.pack(side="right")

    def delett(self):
        self.f.pack_forget()

def addT():
    content=T.get()
    if content !="":
        Newtask=Task(Ouwrapp,content)
        T.delete(0,'end')
    

#------------ Input tasks Frame  ------------
Inwrapp=Frame(win,background=colorPalet['back'])
Inwrapp.pack(fill='both')

T = Entry(Inwrapp,width=40,font="sans-serif",background=colorPalet['back'],fg=colorPalet['front'])
T.pack(side="left",padx=10,pady=10)

addTask=Button(Inwrapp,text="+", width=5,command=addT,background=colorPalet['front'],borderwidth=0)
addTask.pack(side='right',pady=10,padx=10)



#-----------------Output tasks frame---------------------------------
#Ouwrapp=Frame(win,background=colorPalet['back'])
#Ouwrapp.pack(fill='both',expand='yes',padx=10,pady=10)


canvas =Canvas(win,background=colorPalet["back"])
scrollbar = Scrollbar(win, orient="vertical", command=canvas.yview)
Ouwrapp = Frame(canvas,background=colorPalet['back'])

Ouwrapp.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((10, 10), window=Ouwrapp, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#------------------------


win.mainloop()
win.destroy()