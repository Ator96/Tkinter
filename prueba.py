from tkinter import *

#Zona de clases


#Zona de funciones
#Ejemplo
def Hello():
    det=Tk()
    frame = Frame(det)
    lan = ["Python", "C++", "iOS", "Swift"]
    d = 1;

    list = Listbox(frame)
    for i in lan:
        list.insert(d, i)
        d += 1
    frame.pack()
    list.pack()
    det.mainloop()



#Ventana
root = Tk()

#Declaracion de variables
ment = StringVar()

#Metadatos
root.title("Diccionario")
root.geometry("400x300+50+50")

# Declaración de Marcos

topFrame = Frame(root)
topFrame.pack(fill=BOTH)  # Primer Frame
middleFrame = Frame(root)
middleFrame.pack(fill=BOTH)  # Marco del centro
bottonFrame = Frame(root)
bottonFrame.pack(side=BOTTOM, fill=BOTH)  # Marco del final

# Labels
label1 = Label(topFrame,text="Primer proyecto de Estructura de Datos y Algoritmos II\nOscar Gutiérrez Castillo\nCarlos Arrileta")

# Inputs
input = Entry(middleFrame, textvariable=ment).pack()

# Botones
buscar = Button(middleFrame, text="Buscar", fg="red", command=Hello)
agregar = Button(middleFrame, text="Agregar", fg="blue")
eliminar = Button(middleFrame, text="Eliminar", fg="green")
cargar = Button(bottonFrame, text="Cargar", fg="purple")
guardar = Button(bottonFrame, text="Guardar")
salir = Button(bottonFrame, text="Salir", command=sys.exit)

# Paquetes
label1.pack()
buscar.pack()
agregar.pack(side=LEFT)
eliminar.pack(side=RIGHT)
cargar.pack()
guardar.pack()
salir.pack(side=BOTTOM)


#Lanzador
root.mainloop()
