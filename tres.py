from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()

two = Label(root, text="One", bg="green", fg="white")
two.pack(fill=X)

three = Label(root, text="One", bg="blue", fg="white")
three.pack(fill=Y, side=LEFT)



root.mainloop()

