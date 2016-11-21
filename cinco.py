from tkinter import *
root = Tk()


def printName(event):
    print("Hi, my name is Oscar");
#button1 = Button(root, text="Print my name", command = printName())
button1 = Button(root,text="Print my name" )
button1.bind("<Button-1>", printName)
button1.pack()


root.mainloop()