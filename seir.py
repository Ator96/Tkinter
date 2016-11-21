from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

def middleClick(event):
    print("Middle")

frame = Frame(root, width=300 ,height=400)
frame.bind("<Button-1>", leftClick) #Boton izquierdo del mouse
frame.bind("<Button-2>", middleClick) #Boton central del mouse
frame.bind("<Button-3>", rightClick) #Boton derecho del mouse
frame.pack()


root.mainloop()