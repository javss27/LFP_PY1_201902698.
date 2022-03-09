
from sunau import AUDIO_UNKNOWN_SIZE
from tkinter.filedialog import askopenfilename
from  Token import Token



class AnalizadorLexico:
    def guardar(self, lexema, tipo, posicion, linea):
        self.listaTokens.append(Token(lexema,tipo, posicion, linea))
      

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
        self.iniciarAnalisis()
    

    def analizador(self,contenido):
        contenido = contenido.replace(" ","").replace("   ","")
        estado = 0
        posicion = 0
        linea = 0
        aux = ""

        for caracter in contenido:
            print(estado)
            if caracter == "\n":
                linea += 1
                posicion =0
            elif estado == 0:
                aux += caracter
                posicion +=1
                if aux == "formulario":
                    self.guardar(aux,"formulario",posicion, linea)
                    estado = 1
                    aux =""
            elif estado == 1:
                aux += caracter
                posicion += 1
                
                if aux == "~>>":
                    self.guardar(aux,"palabra reservada", posicion, linea)
                    estado = 2
                    aux =""
            elif estado == 2:
                posicion +=1
                if caracter == "[":
                    self.guardar(caracter,"corchete", posicion, linea)
                    estado = 3
            elif estado == 3:
                posicion +=1
                if caracter == "<":
                    self.guardar(caracter,"menor", posicion, linea)
                    estado = 4
            elif estado == 4: #este es para todos tipo, valor, fondo, valores, evento 
                aux += caracter
                posicion += 1
                
                if aux == "tipo:":
                    self.guardar(aux,"tipo:", posicion, linea)
                    estado = 5
                    aux = ""
                elif aux == "valor:":
                    self.guardar(aux,"valor:", posicion, linea)
                    estado = 6
                    aux = ""
                elif aux == "fondo:":
                    print("estamos here")
                    self.guardar(aux,"fondo:", posicion, linea)
                    estado = 6
                    aux =""
                elif aux == "valores:":
                    self.guardar(aux,"valores:", posicion, linea)
                    estado = 9
                    aux = ""
                elif aux == "evento:":
                    self.guardar(aux,"evento:", posicion, linea)
                    estado =10 
                    aux =""
                elif aux == "nombre:":
                    self.guardar(aux, "nombre:", posicion, linea)
                    estado = 6
                    aux = ""

            elif estado == 6:
                aux += caracter
                posicion += 1
                if aux[0] == '"':
                    estado = 11
                    aux =""

            #continuar con 
            elif estado == 5:
                aux += caracter
                posicion += 1
                if aux == '"etiqueta"':
                    self.guardar(aux,"etiqueta:", posicion, linea)
                    estado = 14
                    aux = ""
                elif aux == '"texto"':
                    self.guardar(aux,"texto", posicion, linea)
                    estado = 14
                    aux = ""
                elif aux == '"grupo-radio"':
                    self.guardar(aux,"grupo-radio", posicion, linea)
                    estado = 14 
                    aux = ""
                elif aux == '"grupo-option"':
                    self.guardar(aux,"grupo-option", posicion, linea)
                    estado = 14
                    aux = ""
                elif aux == '"boton"':
                    self.guardar(aux,"boton",posicion,linea)
                    estado = 14
                    aux = ""
            #Continuar con los que faltan
            elif estado == 11:
                aux += caracter
                posicion += 1
                if caracter == '"':
                    self.guardar(aux, "texto", posicion, linea)
                    estado = 14
                    aux =""
            elif estado == 7:
                if caracter == ",":
                    self.guardar(caracter, "coma", posicion, linea)
                    estado = 3
                    aux =""
                elif caracter == "]":
                    self.guardar(caracter, "cocheteOut", posicion, linea)
                    estado = 3
                    aux =""
            elif estado == 9:
                aux += caracter
                posicion += 1
                if caracter == "[":
                    self.guardar(caracter, "CorchetIni", posicion, linea)
                    estado = 12
            
            elif estado == 12:
                aux += caracter
                posicion += 1
                if caracter == "'":

                    estado = 13
                    aux =""
            
                elif aux ==",":
                    self.guardar(caracter,"coma", posicion, linea)
                    estado = 12
                    aux =""
                elif aux == "]":
                    self.guardar(caracter,"CorchetFin", posicion, linea)
                    estado = 14
                    aux = ""
            elif estado == 13:
                aux += caracter
                posicion += 1
                if caracter == "'":
                    self.guardar(aux, "comilla", posicion, linea)
                    estado = 12
                    aux =""
            elif estado == 14:
                aux += caracter
                posicion +=1
                if aux == ",":
                    self.guardar(caracter,"coma", posicion, linea)
                    estado = 4
                    #regresando al estado 4
                    aux=""
                elif aux == ">":
                    self.guardar(caracter,"mayor", posicion, linea)
                    estado = 7
                    aux = ""
            elif estado == 10:
                aux += caracter
                posicion += 1
                if aux== "<entrada>":
                    self.guardar(aux, "<entrada>", posicion, linea)
                    estado= 14
                    aux = ""
                if aux== "<info>":
                    self.guardar(aux, "<info>", posicion, linea)
                    estado= 14
                    aux= ""

        for Token in self.listaTokens:
            print(Token.lexema,",",Token.linea, Token.columna)        
