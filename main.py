# icons form 

# <a href="https://www.flaticon.com/fr/icones-gratuites/ecrivain" title="écrivain icônes">Écrivain icônes créées par Freepik - Flaticon</a>




from ctypes import pointer
from tkinter import *
from turtle import bgcolor
from tools import *

###########################################
#-------window configuration -----------

win=Tk() 
win.geometry("500x500")
win.resizable(False,False)
win.title("TO DO")
img = PhotoImage(file='icon.png')
win.tk.call('wm', 'iconphoto', win._w, img)
col=win['background']


def addT(e):
    content=T.get()
    if content !="":
        Newtask=Task(Ouwrapp,content)
        addTofile(content)
        T.delete(0,'end')

#----------------------- Input tasks Frame  --------------------------------

Inwrapp=Frame(win)
Inwrapp.pack(fill='both')
T = Entry(Inwrapp,width=40,font="sans-serif",borderwidth=0.5,bg="#EFEFEF")
T.pack(side="left",padx=10,pady=10,fill=Y)
T.bind("<Return>",addT)

addTask=Button(
                Inwrapp,text="+",
                width=5,command=addT,
                bg="orange",
                fg="white",
                border=0,
                activebackground='orange',
                activeforeground="white",
                cursor="hand2")

addTask.pack(side='right',pady=10,padx=10,fill=Y)


#-------------------------Output tasks frame---------------------------------

canvas =Canvas(win,borderwidth=0)
Ouwrapp = Frame(canvas)
canvas.create_window((10, 10), window=Ouwrapp, anchor="nw")
canvas.pack(side="left", fill="both", expand=True)
scrollbar = Scrollbar(win, orient="vertical", command=canvas.yview)
Ouwrapp.bind( "<Configure>",lambda e: canvas.configure( scrollregion=canvas.bbox("all")))
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

#------------------------

readAllfile(Ouwrapp)   # whith open get all tasks from fils


win.mainloop()
win.destroy()