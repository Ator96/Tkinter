from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.font import Font
"""
Programa realizador por Oscar Gutierrez Castillo, Carlos Alberto Hernandez Arrieta, Axel Mauricio Hernandez Lopez y Alexis Saul Dominguez Cisneros
Este programa buscar ser in ontermediario para poder buscar, agregar y eliminar palabrar almacenadas en un docuemtno de texto
La parte funcional fue implementada con el uso de una estructura Arbol para poder secuenciar letra por letra, ya que al momento de buscar se permite entregrar
al usuario coincidencias parecidas a la palabra ingresada.

Otra particularidad de este programa es el uso de metodos de busqueda en arboles para poder obtener los datos solicitados.

"""
class Nodo:
	"""docstring for Nodo
	Estructura base para todo el arbol
	Encapsula todos los datos de la estructura nodo

	"""

	def __init__(self, id):
		"""
		Contruye un nuevo nodo
		:param id:Recibe el caracter de la palabra
		"""
		self.id =id.lower()
		self.parent = None 
		self.hijos={}
		self.visitado = False
		self.nivel = -1
		self.parent = None
		self.definicion = None
	def agregarVecino(self,vecino):
		"""
		:param vecino: Verifica que el nodo que recibe no este en su lista de hijos en caso de no estarlo, lo agrega
		"""
		if( vecino.id not in self.hijos):
			self.hijos[vecino.id]=vecino
class Arbol:
	"""
	Estructura principal del programa
	Se hacen los procesaminetos de los datos que se reciben así como las muestras y las eliminaciones
	"""
	def __init__(self):
		"""
		Contruye un nuevo arbol
		No recibe parametros ya que al iniciarse, se manera automática genera un nodo padre
		"""
		self.raiz = Nodo("-")

	def insertarEnArbol(self,palabra,definicion):
		"""
		Funcion encargada de recibir las palabrar con sus respectivas definiciones para ingresarlas al arbol
		:param palabra: Palabra a insertar en el arbol, debe de seguir un estarndar
		:param definicion: Palabra descriptora de la palabra, esta no sigue un estandar
		"""
		raiz = self.raiz
		palabra = palabra.lower()
		for i in palabra:
			charDeLaPalabra =Nodo(i)
			charDeLaPalabra.parent = raiz
			raiz.agregarVecino(charDeLaPalabra)
			#print(raiz.hijos.keys())
			raiz = raiz.hijos[i]
		raiz.definicion=definicion
		self.BFS("-")


	def BFS(self,raiz):
		"""
		"""
		if(raiz in self.raiz.hijos or raiz == "-"):
			cola=[]
			if(raiz == "-"):
				cola.append(self.raiz)
				self.raiz.nivel=0
				print("("+str(self.raiz.id)+", "+str(self.raiz.nivel)+")")
			else:
				cola.append(self.raiz.hijos[raiz])
				self.raiz.hijos[raiz].nivel = 0
				print("("+str(self.raiz.hijos[raiz].id)+", "+str(self.raiz.hijos[raiz].nivel)+")")
			while(len(cola)>0):
				actual = cola[0]
				cola = cola[1:]
				for hijo in actual.hijos.values():
					cola.append(hijo)
					hijo.nivel = actual.nivel +1
					print("("+hijo.id+", "+str(actual.hijos[hijo.id].nivel)+" "+str(actual.hijos[hijo.id].definicion) + ")")

		else:
			print("Nada")

	def buscarPalabra(self,palabra,i,raiz):
		"""
		Funcion que busca la palabra que el usuario desee, busca en todo el arbol de manera dirigida buscado en la ruta que que marcan los caracteres de la palabra,
		en caso de que no se encuentre el siguiente caracter, genra un subarbol temporal y empieza a sacar todas las coincidencias que existen, en caso de no existir subarbol se asume que no hay nada perecido
		:param palabra: palabra a buscar
		:param i:posion donde nos encontramos parados, esta es default y ayuda a la busqueda orientada
		:param raiz: Raiz padre (actual) donde se buscan al hijo caracter que coincida 
		"""
		if( i != len(palabra) and (palabra[i] in raiz.hijos) ):
			if( (i == len(palabra)-1) and raiz.hijos[ palabra[i] ].definicion != None):
				print(palabra)
				print(raiz.hijos[ palabra[i] ].definicion)
				print("\n")
				return [[palabra,raiz.hijos[ palabra[i] ].definicion],False]
			else:
				i=i+1
				return self.buscarPalabra(palabra,i,raiz.hijos[ palabra[i-1] ])
		elif(raiz.id == "-"):
			print(i,raiz.id)
			cadena = ""
			coincidencias=self.DFS(raiz,cadena,[])

			#self.subArbolDeCoincidencias(raiz)
			#no existe la esa letra en esa subarbol 
			#hacer recorrido DFS
			return [coincidencias,True]

		else: 
			print(palabra[0:i])
			print(i,raiz.id)
			cadena = palabra[0:i-1]
			print(cadena+"\n")
			coincidencias=self.DFS(raiz,cadena,[])
			#self.subArbolDeCoincidencias(raiz)
			#no existe la esa letra en esa subarbol 
			#hacer recorrido DFS
			return [coincidencias,True]

	
	def DFS(self,nodo,cadena,lista):
		"""
		Cuando no se encuentra la siguiente letra en la palabra a buscar, se inicia esta funcion, se encarga de buscar todas las conbinaciones que existen
		
		"""
		if(nodo.id != "-"):
			cadena = cadena + nodo.id
		for vertice in nodo.hijos:
				lista=self.DFS(nodo.hijos[vertice],cadena,lista)	
		if(nodo.definicion != None):
			lista.append([cadena,nodo])
			print(cadena)
			print(nodo.definicion)
		return lista

	def subArbolDeCoincidencias(self,raiz):
		cola=[]
		cola.append(raiz)
		raiz.nivel=0
		#print("("+str(raiz.id)+", "+str(raiz.nivel)+" "+str(raiz.definicion)+")")
		while(len(cola)>0):
			actual = cola[0]
			cola = cola[1:]
			for hijo in actual.hijos.values():
				cola.append(hijo)
				hijo.nivel = actual.nivel +1
				#print("("+hijo.id+", "+str(actual.hijos[hijo.id].nivel)+" "+str(actual.hijos[hijo.id].definicion) + ")")

	def Existencia(self,palabra,i,raiz):
		ultimoNodo = None
		if( i != len(palabra) and (palabra[i] in raiz.hijos) ):
			if( (i == len(palabra)-1) and raiz.hijos[ palabra[i] ].definicion != None):
				print(raiz.hijos[ palabra[i] ].definicion)
				ultimoNodo = raiz.hijos[ palabra[i] ]
				return ultimoNodo
				print("\n")
			else:
				i=i+1
				return self.Existencia(palabra,i,raiz.hijos[ palabra[i-1] ])
		#else:
		#	print("devolvi nada")
		#	return None
		

	def ExistePalabra(self,palabra):
			palabra=palabra.lower()
			#print("entre aqui")
			existenciaDePalabra = self.Existencia(palabra,0,self.raiz)
			if(existenciaDePalabra != None):
				#print("entre aqui en el if")
				definicion = existenciaDePalabra.definicion
				existenciaDePalabra.definicion=None
				self.borrarPalabra(existenciaDePalabra)
				#self.BFS("-")
				print("\n")
				tkinter.messagebox.showinfo('Aviso','la palabra '+palabra+ ' fue borrada')
			else:
				print("Palabra No existe en el diccionario")
				tkinter.messagebox.showinfo('Aviso','la palabra '+palabra+' no existe en el diccionario')	


	def borrarPalabra(self,nodo):
		if( len(nodo.hijos) == 0 and nodo.parent != None):
			print("el padre es "+str(nodo.parent.id)+"\n")
			print("y sus hijos son"+str(nodo.parent.hijos[nodo.id].id))
			del nodo.parent.hijos[nodo.id]
			self.borrarPalabra(nodo.parent)
		else:
			print("Termino de borrar Palabra")


			
		
#Seccion de lectura y guardado en archivo
	
	def DFSguardar(self,nodo,cadena,lista):
		if(nodo.id != "-"):
			cadena = cadena + nodo.id
		for vertice in nodo.hijos:
				self.DFSguardar(nodo.hijos[vertice],cadena,lista)
		if(nodo.definicion != None):
			lista.append(cadena + ":" + nodo.definicion + "\n")
		return lista
			
	def guardarArbolEnArchivo(self,nombre):
		lista = []
		cadena = ""
		try:
			archivo = open(nombre + ".txt","w")
			#Aqui se guarda la palabra y la definicion dentro del archivo
			lista = self.DFSguardar(self.raiz,cadena,lista)
			archivo.writelines(lista)
			tkinter.messagebox.showinfo('Aviso', 'Diccionario guardado exitosamente')
			
		except Exception as e:
			tkinter.messagebox.showinfo('Aviso', 'Error al guardar el archivo')
			print("Log: Error al abrir archivo " + e)
			
		finally:
			archivo.close()
		
	def leerArbolDeArchivo(self,DirArchivo,raiz):
		#Aqui se crea un nuevo arbol para sustituirlo por el que estaba en uso
		arreglo = []

		try:
			archivo = open(DirArchivo,"r")
			for linea in archivo:
				linea = linea.strip("\n")
				linea = linea.split(":")
				self.insertarEnArbol( linea[0], linea[1] )
			tkinter.messagebox.showinfo('Aviso', 'Diccionario cargado exitosamente')

		except Exception as e:
			tkinter.messagebox.showinfo('Aviso', 'Error al cargar el archivo')
			print("Log: Error al abrir archivo " + e)
			
		finally:
			archivo.close()
		
		
arbol = Arbol()
temporal=None

#Zona de funciones
#Ejemplo
def Hello(s):
    det=Tk()
    frame = Frame(det)
    lan = ["Python", "C++", "iOS", "Swift", s]
    d = 1;

    list = Listbox(frame)
    for i in lan:
        list.insert(d, i)
        d += 1
    frame.pack()
    list.pack()
    det.mainloop()

def insertar(e1,e2):
	global arbol
	arbol.insertarEnArbol(e1.get(),e2.get())
	e1.delete(0,END)
	e2.delete(0,END)

def Agregar():
	global arbol

	master = Tk()
	Label(master, text="Palabra").grid(row=0)
	Label(master, text="Definicion").grid(row=1)
	
	e1 = Entry(master)
	e2 = Entry(master)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	Button(master, text='Salir',bg="red",command=lambda:master.destroy()).grid(row=3, column=0, sticky=W, pady=4)
	Button(master, text='Insertar', command=lambda :insertar(e1,e2) ).grid(row=3, column=1, sticky=W, pady=4)
	
	master.mainloop( )



def Cargar():
	global arbol
	from os import getcwd

	name = askopenfilename(initialdir = getcwd(),
                           filetypes = (("Text File", "*.txt"),("All Files","*.*")),
                           title = "Elige el archivo"
                           )
	if name != "":
		arbol.leerArbolDeArchivo(name,arbol.raiz)

def Guardar():
	global arbol
	from os import getcwd

	name = asksaveasfilename(initialdir = getcwd(),
                           filetypes = (("Text File", "*.txt"),("All Files","*.*")),
                           title = "Elige nombre del archivo"
                           )
	if name != "":	
		arbol.guardarArbolEnArchivo(name)
		
def borrar(e1):
	global arbol
	arbol.ExistePalabra(e1.get())
	e1.delete(0,END)
	
def Eliminar():
	global arbol

	master = Tk()
	Label(master, text="Palabra").grid(row=0)
	
	e1 = Entry(master)
	e1.grid(row=0, column=1)
	Button(master, text='Salir',bg="red", command=lambda:master.destroy()).grid(row=3, column=0, sticky=W, pady=4)
	Button(master, text='Borrar', command=lambda :borrar(e1) ).grid(row=3, column=1, sticky=W, pady=4)
	
	master.mainloop( )

def on_select(event):
	global temporal
	top = Tk()
	Lb1 = Listbox(top,width=70, height=30)
	palabra=temporal[event.widget.curselection()[0]][0]
	definicion=temporal[event.widget.curselection()[0]][1].definicion
	Lb1.insert(1,palabra)
	Lb1.insert(2,definicion)
	Lb1.pack()
	top.mainloop()
def Buscar():
	global arbol
	global temporal
	palabra = ment.get()
	coincidencias=arbol.buscarPalabra(palabra.lower(),0,arbol.raiz)
	#print(coincidencias)
	if(coincidencias[1] != False):
		temporal=coincidencias[0]
		i=0
		palabra=""
		definicion=""
		root = Tk()
		scrollbar = Scrollbar(root, orient="vertical")	
		lb = Listbox(root, width=50, height=20, yscrollcommand=scrollbar.set)
		scrollbar.config(command=lb.yview)
		scrollbar.pack(side="right", fill="y")
		scrollbar.pack(side="right", fill="y")
		lb.pack(side="left",fill="both", expand=True)
		lb.bind('<<ListboxSelect>>',on_select)
		for i in range(len(coincidencias[0])):
			palabra=coincidencias[0][i][0]
			definicion=coincidencias[0][i][1].definicion
			lb.insert("end", "palabra "+str(i)+" %s" %palabra)
			
		root.mainloop()
	else:
		top =Tk()
		Lb1 = Listbox(top,width=70, height=30)
		Lb1.insert(1, coincidencias[0][0])
		Lb1.insert(2,"Definicion: "+coincidencias[0][1])
		Lb1.pack()
		top.mainloop()

#Ventana
root = Tk()



#Intancia del arbol


#Declaracion de variables
ment = StringVar()

#Metadatos
root.title("Diccionario")
#la linea de abajo esta comentada porque solo cambia de color una pequeña parte de la interfaz entre las dos imagenes
#root.config(bg="grey") 
root.geometry("400x300+50+50")
#imagenes
imagenL=PhotoImage(file="UNAM.gif")
lblImagen=Label(root,image=imagenL).place (x=5,y=130)
imagenF=PhotoImage(file="fi.gif")
lblImagen=Label(root,image=imagenF).place (x=300,y=130)


#Declaracion de Marcos

topFrame = Frame(root)
topFrame.pack(fill=BOTH)  # Primer Frame
middleFrame = Frame(root)
middleFrame.pack(fill=BOTH)  # Marco del centro
bottonFrame = Frame(root)
bottonFrame.pack(side=BOTTOM, fill=BOTH)  # Marco del final

# Labels
label1 = Label(topFrame,text="Primer proyecto de Estructura de Datos y Algoritmos II\nOscar Gutiérrez Castillo\nCarlos Alberto Hernandez Arrieta\nAxel Mauricio Hernandez Lopez\nAlexis Saul Domínguez Cisneros",font=("Helvetica",10))

# Inputs
input = Entry(middleFrame, textvariable=ment).pack()

# Botones
buscar = Button(middleFrame, text="Buscar", relief="raised",fg="darkred", command=Buscar)
agregar = Button(bottonFrame, text="Agregar", fg="blue4", command=Agregar)
eliminar = Button(bottonFrame, text="Eliminar", fg="green4", command=Eliminar)
cargar = Button(bottonFrame, text="Cargar", fg="orange", command=Cargar)
guardar = Button(bottonFrame, text="Guardar", command=Guardar)
salir = Button(bottonFrame, text="Salir",bg="red" ,command=sys.exit)

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
