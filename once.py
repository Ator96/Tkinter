from tkinter import *
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo('Window Tittle', 'Mokney can fly')


answer = tkinter.messagebox.askquestion('Question1', 'Love me')
if answer == 'yes':
    print("OMG")
tkinter.messagebox._show("Prueba","Algo","fd",)

root.mainloop()