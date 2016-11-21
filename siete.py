from tkinter import  *


class OscarButtion:

    def __init__(self, master):
        frame = Frame(master, width=200, height=300)
        frame.pack()

        self.printButton = Button(master, text="Print Mesasage", command = self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(master, text="Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("This work!")

root = Tk()
instance = OscarButtion(root)
root.mainloop()