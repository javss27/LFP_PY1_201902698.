
import sys 
from logging import root

from click import command

from matplotlib import ticker

from matplotlib.pyplot import inferno
from analizadorLexico import AnalizadorLexico

from tkinter import Tk, Label, Button
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename



class interfazGrafica():
    

    
    def  __init__(self, master):
        
    
        self.master = master
        self.analizadorLexico = AnalizadorLexico()
        master.title("Proyecto 1 LFP")
        
        self.etiqueta = Label(master, text="****MENÚ****")
        self.etiqueta.pack()
        #boton analizar
        self.botonAnlizar = Button(master, text="Analizar Archivo",   )
        self.botonAnlizar.pack()
        self.botonAnlizar.place(x=60,y=40)
        self.botonAnlizar.config(width=12, height=3)
        
        #boton cargar
        
        self.botonCargar = Button(master, text="Cargar Archivo", command = self.obtenerTexto() )
        self.botonCargar.pack()
        self.botonCargar.place(x=170,y=40)
        self.botonCargar.config(width=12, height=3)
        
        #boton Reporte tokens
        self.botonTokens = Button(master, text="Reporte Tokens", )
        self.botonTokens.pack()
        self.botonTokens.place(x= 270,y=40)
        self.botonTokens.config(width=12, height=3)
        #boton reporte errores
        self.botonErrores = Button(master, text="Reporte Errores", )
        self.botonErrores.pack()
        self.botonErrores.place(x= 370,y=40)
        self.botonErrores.config(width=12, height=3)
        #boton reporte Manual tecnico
        self.botonManual = Button(master, text="Manual de Usuario", )
        self.botonManual.pack()
        self.botonManual.place(x=470,y=40)
        self.botonManual.config(width=13, height=3)
        #boton reporte Manual usuario
        self.botonManualUsuario = Button(master, text="Manual Tecnico", )
        self.botonManualUsuario.pack()
        self.botonManualUsuario.place(x=575,y=40)
        self.botonManualUsuario.config(width=12, height=3)
        
        #area de texto 
        texto = Text(root)
        texto.pack()
        texto.config(width=67, height=10, font=("Consolas",12), 
             padx=0, pady=15)
        texto.place(x=60,y=100)
        texto.insert(INSERT, self.texto  )
    
    def obtenerTexto(self):
        self.texto = self.analizadorLexico.leerArchivo(askopenfilename())


                                    
 
root = Tk()
miVentana = interfazGrafica(root)
root.geometry('720x480')
root.mainloop()
