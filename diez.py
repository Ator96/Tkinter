from tkinter import *
import sys

def Hello():
    mText = ment.get()
    mlabel2 = Label(root, text=mText).pack()


root = Tk()
ment = StringVar()
root.title('Diez')

mButton = Button(root, text='OK', command=Hello).pack()
input = Entry(root, textvariable=ment).pack()


root.mainloop()



