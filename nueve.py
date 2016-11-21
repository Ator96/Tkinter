from tkinter import *

def doNothing():
    print("ok ok I won't...")

root = Tk()

menu1 = Menu(root)
root.config(menu=menu1)


submenu = Menu(menu1)
menu1.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project...", command=doNothing)
submenu.add_command(label="New...", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu1)
menu1.add_cascade(label="Edit", menu=submenu)
submenu.add_command(label="Edit Project...", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=doNothing)

root.mainloop()
