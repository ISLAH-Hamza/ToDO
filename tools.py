from textwrap import fill
from tkinter import *
from typing import Counter
#--------------------class and function definition-------------------
datafile='data/dataTask.txt'  
class Task:
    def __init__(self,parent,content):
        self.content=content
        self.f=Frame(parent,bg="#086E7D")
        self.f.pack(pady=2)
        
        self.label=Label(
            self.f,
            text=content,
            width=50,
            bg="#086E7D",fg="white")
        
        self.label.pack(side="left",fill=Y)

        self.butotn=Button(
            self.f,
            text="delete",
            command=self.delett,
            bg="#086E7D",
            fg="white",
            borderwidth=0,
            activebackground="#086E7D",
            activeforeground="orange"
            )
        self.butotn.pack(side="right",fill=Y)
    def delett(self):
        self.f.pack_forget()
        removefromfile(self.content)


#load all task from data file to the Gui app
def readAllfile(output):
    try:
        fil=open(datafile,'r')
        content=fil.readlines()
        for elem in content:
            elem=elem.replace("\n","")
            Newtask=Task(output,elem)
        fil.close()
        pass
    except  FileNotFoundError:
        fil=open(datafile,'w')


# remove tasks from data file
def removefromfile(content):
    try:
        fil=open(datafile,'r')
        lines=fil.readlines()
        s=content
        try:
            lines.pop(lines.index(s))
        except:
            try:
                lines.pop(lines.index(s+'\n'))
            except:
                pass
        fil.close()
    except FileNotFoundError:
        print('the file is empty')
    with open(datafile,'w') as fil:
        fil.writelines(lines)


# adding a new task to data file

def addTofile(content):
    try:
        fil=open(datafile,'r')
    except  FileNotFoundError:
        fil=open(datafile,'w')
    lines=fil.readlines()
    fil.close()
    s=content+'\n'
    if s not in lines:
        lines.append(s)
    with open(datafile,'w') as fil:
        fil.writelines(lines)
