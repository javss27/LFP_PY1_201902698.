
from logging import root

from turtle import back
from webbrowser import BackgroundBrowser
import webbrowser

from click import command
from flask import Blueprint

from matplotlib import ticker

from matplotlib.pyplot import inferno
from analizadorLexico import AnalizadorLexico

from tkinter import Tk, Label, Button
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from Token import Error


class interfazGrafica():
    
    

    
    def  __init__(self, master):

        self.textoCargado = ""
        self.texto = "" 
        self.master = master
        self.analizadorLexico = AnalizadorLexico()
        
        
        self.etiqueta = Label(master, text="Menú", background= "#95E7E7")
        self.etiqueta2 = Label(master,text= "Selecciona la opcion a realizar.",padx=10,pady=1,background= "#95E7E7")
        self.etiqueta.pack()
        self.etiqueta2.pack()
        #boton analizar
        self.botonAnlizar = Button(master, text="Analizar Archivo", command = self.analizar,background="#3B89DC")
        self.botonAnlizar.pack()
        
        self.botonAnlizar.place(x=164,y=45)
        self.botonAnlizar.config(width=12, height=3)
        
        #boton actualizar .form
        self.botonActualizar = Button(master, text="Actualizar Archivo", command = self.actualizarArchivo,background="#3B89DC" )
        self.botonActualizar.pack()
        self.botonActualizar.place(x=60,y=340)
        self.botonActualizar.config(width=13, height=3)

        #boton cargar
        
        self.botonCargar = Button(master, text="Cargar Archivo", command = self.obtenerTexto, background="#3B89DC")
        self.botonCargar.pack()
        
        self.botonCargar.place(x=60,y=45)
        self.botonCargar.config(width=12, height=3)
        
        
        #boton Reporte tokens
        self.botonTokens = Button(master, text="Reporte Tokens", command = self.reporteTokens, background="#3B89DC" )
        self.botonTokens.pack()
        self.botonTokens
        self.botonTokens.place(x= 270,y=45)
        self.botonTokens.config(width=12, height=3)
        #boton reporte errores
        self.botonErrores = Button(master, text="Reporte Errores", command = self.reporteErrores, background="#3B89DC" )
        self.botonErrores.pack()
        self.botonErrores.place(x= 370,y=45)
        self.botonErrores.config(width=12, height=3)
        #boton reporte Manual tecnico
        self.botonManual = Button(master, text="Manual Tecnico", background="#3B89DC", command = self.manualTecnico )
        self.botonManual.pack()
        self.botonManual.place(x=470,y=45   )
        self.botonManual.config(width=13, height=3)
        #boton reporte Manual usuario
        self.botonManualUsuario = Button(master, text="Manual de Usuario", background="#3B89DC", command= self.manualUsuario )
        self.botonManualUsuario.pack()
        self.botonManualUsuario.place(x=575,y=45)
        self.botonManualUsuario.config(width=12, height=3)
        # boton terminar programa
        self.botonSalir = Button(master, text="Salir", background="#3B89DC", command= exit)
        self.botonSalir.pack()
        self.botonSalir.place(x=597,y=340)
        self.botonSalir.config(width=8, height=3)
    
    
       
        #area de texto 
        self.textoDos = Text(root)
        self.textoDos.pack()
        self.textoDos.config(width=67, height=10, background= "white" ,font=("Consolas",12), 
             padx=0, pady=15)
        self.textoDos.place(x=60,y=105)
        self.textoDos.insert(INSERT, self.texto  )
    
    def obtenerTexto(self):
        
        self.texto = self.analizadorLexico.leerArchivo(askopenfilename())
        self.textoDos.insert(INSERT, self.texto  )

    def analizar(self):
        self.analizadorLexico.iniciarAnalisis(self.textoDos.get("1.0","end"))
    
    def actualizarArchivo(self):
        result = self.textoDos.get("1.0","end")
        print(result)

    def reporteTokens(self):
        self.analizadorLexico.listaTokens
        #para crear el html 
        tokens = '<!DOCTYPE html> <html lang="es"> <head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>REPORTE</title><linkhref="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css"rel="stylesheet"integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU"crossorigin="anonymous"/><body><h1 class="text-center">Reporte Tokens</h1><hr /><div class="m-2 p-2"><table class="table table-striped"><thead><tr> <tr> <th scope="col">Token.</th><th scope="col">Lexema</th><th scope="col">Fila.</th><th scope="col">Columna.</th></tr></thead><tbody>'
        for Token in self.analizadorLexico.listaTokens:
            tokens +='<tr> <td>'+ str(Token.tipo) +'</td> <td>'+ str(Token.lexema) +'</td><td>'+ str(Token.linea) +'</td><td>'+ str(Token.columna) +'</td></tr>'
        tokens += '</tbody></table> </div><hr /><scriptsrc="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"  crossorigin="anonymous"></script></body></html>'
        # Abriendo el archivo en modo de escritura
        file = open('reporteTokens.html', "w")
        file.write(tokens)
        file.close()
      
    #para los errores igual que con tokens pero con variable errores
    #como sobre escribir un archivo txt
    def reporteErrores(self):
        self.analizadorLexico.listaErrores
        erroress  = '<!DOCTYPE html> <html lang="es"> <head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>REPORTE</title><linkhref="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css"rel="stylesheet"integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU"crossorigin="anonymous"/><body><h1 class="text-center">Reporte Errores</h1><hr /><div class="m-2 p-2"><table class="table table-striped"><thead><tr> <tr> <th scope="col">Errores Lexicos.</th><th scope="col">Caracter</th><th scope="col">Fila.</th><th scope="col">Columna.</th></tr></thead><tbody>'
        for  Error in self.analizadorLexico.listaErrores:
            erroress += '<tr> <td>'+ str(Error.lexema) +'</td> <td>'+ str(Error.tipo) +'</td><td>'+ str(Error.linea) +'</td><td>'+ str(Error.columna) +'</td></tr>'
        erroress += '</tbody></table> </div><hr /><scriptsrc="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"  crossorigin="anonymous"></script></body></html>'
        # Abriendo el archivo en modo de escritura
        file = open('reporteErrores.html', "w")
        file.write(erroress)
        file.close()

    def manualUsuario(self):
        webbrowser.open_new(r'ManualDeUsuarioProyecto1.pdf')
        

    def manualTecnico(self):
        
        webbrowser.open_new(r'ManualtecnicoProyecto1.pdf')
        
       
      
    
    
    
      
      
    
    
 
root = Tk()
miVentana = interfazGrafica(root)
root.configure(background= "#95E7E7" )
root.geometry('720x480')
root.mainloop()
