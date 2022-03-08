
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
            if caracter == "\n":
                linea += 1
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

            elif estado == 6:
                aux += caracter
                posicion += 1
                if aux[0] == aux[aux.lenght-1]:
                    self.guardar(aux,"texto", posicion, linea)
                    estado = 6
                    aux =""
                elif aux ==",":
                    self.guardar(caracter,"coma", posicion, linea)
                    estado == 4
                    aux =""
                elif aux == ">":
                    self.guardar(caracter,"mayor", posicion, linea)
                    estado = 7
                    aux = ""
            

            #continuar con 
            elif estado == 5:
                aux += caracter
                posicion += 1
                if aux == '"etiqueta"':
                    self.guardar(aux,"etiqueta:", posicion, linea)
                    estado = 5
                    aux = ""
                elif aux == '"texto"':
                    self.guardar(aux,"texto", posicion, linea)
                    estado = 5
                    aux = ""
            #Continuar con los que faltan
                elif caracter == ",":
                    self.guardar(caracter,"coma", posicion, linea)
                    estado == 4
                    #regresando al estado 4
                    aux=""
                elif aux == ">":
                    self.guardar(caracter,"mayor", posicion, linea)
                    estado = 7
                    aux = ""

        for Token in self.listaTokens:
            print(Token.lexema)        




                    
            

                

