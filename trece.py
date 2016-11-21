import tkinter

class Prompt:
    def button_action(self):
        self.my_entry = self.ent.get() #this is the variable I wanna use in another function

    def __init__(self, den):
        self.lbl = tkinter.Label(den, text="Write Something")
        self.ent = tkinter.Entry(den)
        self.btn = tkinter.Button(den, text="Get That Something", command=self.button_action)
        self.lbl.pack()
        self.ent.pack()
        self.btn.pack()

den = tkinter.Tk()
den.title("Widget Example")
prompt = Prompt(den)
den.mainloop()