from tkinter import *
import tkinter.messagebox



root = Tk()
lan = ["Python","C++", "iOS", "Swift"]
d = 0;
list = Listbox(root)
for i in lan:
    list.insert(d,i)
    d +=1


list.pack()

root.mainloop()