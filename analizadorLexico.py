
from dataclasses import replace
from distutils.log import error
from sunau import AUDIO_UNKNOWN_SIZE
from tkinter.filedialog import askopenfilename
from xml.dom.pulldom import CHARACTERS

from numpy import character
from  Token import Token
from analizadorSintactico import analizadorSintactico 


class AnalizadorLexico:
    def guardar(self, lexema, tipo, posicion, linea):
        self.listaTokens.append(Token(lexema,tipo, posicion, linea))
     
    def errores(self, lexema, tipo, posicion, linea):
        self.listaErrores.append(Token(lexema,tipo, posicion, linea))
      
    def leerArchivo(self, ruta):
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        return contenido

    def iniciarAnalisis(self):
        ruta = askopenfilename()
        leer = self.leerArchivo(ruta)
        self.analizador(leer) 

    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        

   

    def analizador(self,contenido):
        contenido = contenido.replace("   ","")
        estado = 0
        posicion = 0
        linea = 0
        aux = ""
        
        for i in range(len(contenido)):
            caracter = contenido[i]
            #print(estado)
            if caracter == "\n":
                linea += 1
                posicion =0
            elif estado == 0:

                posicion +=1
                if caracter == "<":
                    self.guardar(caracter,"<",posicion, linea)
                    estado = 0
                elif caracter == ">":
                    self.guardar(caracter,">",posicion, linea)
                    estado = 0
                elif caracter == "[":
                    self.guardar(caracter,"[",posicion, linea)
                    estado = 0
                elif caracter == "]":
                    self.guardar(caracter,"]",posicion, linea)
                    estado = 0
                elif caracter == "'":
                
                    estado = 13
                elif caracter == '"':
                    #para eliminar las primeras comillas 
                   
                   #comillas ="'"
                   #caracter = ''.join(x for x in caracter if x not in comillas)
                   estado = 11
                #para quitar las ultimas comillas
                elif caracter == ",":
                    self.guardar(caracter,",",posicion, linea)
                    estado = 0
                elif caracter == "~":
                    self.guardar(caracter,"~",posicion, linea)
                    estado = 0
                elif caracter == ":":
                    self.guardar(caracter,":",posicion, linea)
                    estado = 0
                #para las palabras reservadas
                elif caracter.isalpha():
                    aux += caracter
                    estado = 1
                else:
                    self.errores(caracter,"TipoError",posicion, linea)
                    #agregar donde crea que puede venir un errorxº


                    
            elif estado == 1:
                aux += caracter
                posicion += 1

                if aux == "formulario":
                
                    self.guardar(aux,"formulario", posicion, linea)
                    estado = 0
                    aux =""
                elif aux == "entrada":
                    self.guardar(aux,"entrada", posicion, linea)
                    estado = 0

                    aux =""
                elif aux == "info":
                    self.guardar(aux,"info", posicion, linea)
                    estado = 0
                    aux =""
                elif aux == "tipo":
                    self.guardar(aux,"tipo", posicion, linea)
                    
                    estado = 0
                    aux =""
                elif aux == "valor":
                    if contenido[i+1] == "e":
                        estado = 1
                    else:
                        self.guardar(aux,"valor", posicion, linea)
                        estado = 0
                        aux =""   
                elif aux == "fondo":
                    self.guardar(aux,"fondo", posicion, linea)
                    estado = 0
                    aux =""
                elif aux == "valores":
                    self.guardar(aux,"valores", posicion, linea)
                    estado = 0
                    aux =""
                elif aux == "evento":
                    self.guardar(aux,"evento", posicion, linea)
                    estado = 0
                    aux =""
                elif aux == "nombre":
                    self.guardar(aux,"nombre", posicion, linea)
                    estado = 0
                    aux =""
                elif not caracter.isalpha():
                    estado = 0
                #aca termina el analisis del estado 1 por si vienen errores se agrega el else  
                else:
                    self.errores(caracter,"TipoError",posicion, linea)
                    #agregar donde crea que puede venir un error
            elif estado == 11:
                aux += caracter
                posicion += 1
                
                if caracter == '"':
                    aux = aux.replace('"','')
                    self.guardar(aux, "texto", posicion, linea)
                    estado = 0
                    aux =""
                #Encontrar una forma de no guardar la ultima comilla
            elif estado == 13:
                aux += caracter
                posicion += 1
                
                if caracter == "'":
                    aux = aux.replace("'",'')
                    self.guardar(aux, "texto2", posicion, linea)
                    estado = 0
                    aux =""
        
    
    
        
                
