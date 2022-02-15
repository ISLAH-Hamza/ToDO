# icons form 
# <a href="https://www.flaticon.com/fr/icones-gratuites/ecrivain" title="écrivain icônes">Écrivain icônes créées par Freepik - Flaticon</a>

from tkinter import *
from tools import *

###########################################


colorPalet={'back':'#19282F','front':'#B33030'}
#-------window configuration -----------
win=Tk() 
win.geometry("500x500")
win.resizable(False,False)
win.title("TO DO")
win.config(bg=colorPalet['back'])

def addT():
    content=T.get()
    if content !="":
        Newtask=Task(Ouwrapp,content)
        addTofile(content)
        T.delete(0,'end')

#----------------------- Input tasks Frame  --------------------------------

Inwrapp=Frame(win,background=colorPalet['back'])
Inwrapp.pack(fill='both')


T = Entry(Inwrapp,width=40,font="sans-serif",borderwidth=0)
T.pack(side="left",padx=10,pady=10)

addTask=Button(Inwrapp,text="+", width=5,command=addT,borderwidth=0,bg="white")
addTask.pack(side='right',pady=10,padx=10)

#-------------------------Output tasks frame---------------------------------
canvas =Canvas(win,background=colorPalet["back"],borderwidth=0)
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

readAllfile(Ouwrapp)

win.mainloop()
win.destroy()