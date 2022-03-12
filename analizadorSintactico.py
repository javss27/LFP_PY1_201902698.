





class analizadorSintactico():
    def __init__(self, lista):
        self.lista = lista 
        self.posicion = 0
        self.tipo = ""
        self.valor = ""
        self.fondo= ""
        self.valores =""
        self.nombre =""
        self.evento = ""
        self.resultado = ""
        self.aux = self.lista[self.posicion]
        self.iniciarAnalisis()
        print(self.resultado)

    def obtenerSiguiente(self):
        self.posicion += 1        
        self.aux = self.lista[self.posicion]
        print(self.aux.lexema)
        
    def iniciarAnalisis(self):
        if self.aux.tipo == "formulario":
            self.obtenerSiguiente()
            if self.aux.tipo == "~":
                self.obtenerSiguiente()
                if self.aux.tipo == ">":
                    self.obtenerSiguiente()
                    if self.aux.tipo == ">":
                        self.obtenerSiguiente()
                        if self.aux.tipo == "[":
                            self.obtenerSiguiente()
                            self.resultado += "<!DOCTYPE <html> <head> <title> Mi Página de prueba </title> </head> <body>"
                            self.elementos()

    def escribir(self):
        if self.tipo == "etiqueta":
            self.resultado += "<label> "+ self.valor + "</label>"





    def elementos(self):
        if self.aux.tipo == "<":
            self.obtenerSiguiente()
            self.elemento()
            self.escribir()
        if self.aux.tipo == ">":
            self.obtenerSiguiente()
            if self.aux.tipo == ",":
                self.obtenerSiguiente()
                self.elementos()   
            elif self.aux.tipo == "]":
                self.resultado += "</body> </html>"
                print("terminado")
    
    def elemento(self):
        if self.aux.tipo == "tipo":
            self.obtenerSiguiente()
            if self.aux.tipo == ":":
                self.obtenerSiguiente()
                self.tipos()
                if self.aux.tipo == ",":
                    self.obtenerSiguiente()
                    self.elemento()
                elif self.aux.tipo == ">":
                    return
        elif self.aux.tipo == "valor":
            self.obtenerSiguiente()
            if self.aux.tipo == ":":
                self.obtenerSiguiente()
                if self.aux.tipo == "texto":
                    #aca cambia el self segun lo que quiero 
                    self.valor = self.aux.lexema
                    self.obtenerSiguiente()
                    if self.aux.tipo == ",":
                        self.obtenerSiguiente()
                        self.elemento()
                    elif self.aux.tipo == ">":
                        return
        elif self.aux.tipo == "fondo":
            self.obtenerSiguiente()
            if self.aux.tipo == ":":
                self.obtenerSiguiente()
                if self.aux.tipo == "texto":
                    self.fondo = self.aux.lexema
                    self.obtenerSiguiente()
                    if self.aux.tipo == ",":
                        self.obtenerSiguiente()
                        self.elemento()
                    elif self.aux.tipo == ">":
                        return
        elif self.aux.tipo == "valores":
            self.obtenerSiguiente()
            if self.aux.tipo == ":":

                self.obtenerSiguiente()

                if self.aux.tipo == "[":
                    self.obtenerSiguiente()
                    if self.aux.tipo == "'":
                        self.obtenerSiguiente()
                        if self.aux.tipo == "texto":
                            self.valores = self.aux.lexema
                            self.obtenerSiguiente()
                            if self.aux.tipo == "'":
                                self.obtenerSiguiente()
                                if self.aux.tipo == "]":
                                    self.obtenerSiguiente()
                                    if self.aux.tipo == ",":
                                        self.obtenerSiguiente()
                                
                                        if  self.aux.tipo == "]":
                                            self.obtenerSiguiente()
                                            self.elemento()
                                        elif self.aux.tipo == ">":
                                            
                                            return
        elif self.aux.tipo == "evento":
            self.obtenerSiguiente()
            if self.aux.tipo == ":":
                self.obtenerSiguiente()
                if self.aux.tipo == "<":
                    self.obtenerSiguiente()
                    if self.aux.tipo == "texto":
                        self.evento = self.aux.lexema
                        self.obtenerSiguiente()
                        if self.aux.tipo == ">":
                            self.obtenerSiguiente()
                            if self.aux.tipo == ",":
                                self.obtenerSiguiente()
                                self.elemento()
                            elif  self.aux.tipo == "]":
                                return



            
                
    def tipos(self):
        print(self.aux.lexema)
        if self.aux.lexema == "etiqueta":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
        elif self.aux.lexema == "grupo-radio":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
        elif self.aux.lexema ==  "grupo-option":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
        elif self.aux.lexema == "boton":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()

    def tiposDos(self):
        print(self.aux.lexema)
        if self.aux.lexema == "entrada":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
        elif self.aux.lexema == "info":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()




                    

                        



