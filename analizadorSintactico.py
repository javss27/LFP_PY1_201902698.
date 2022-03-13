





class analizadorSintactico():
    def __init__(self, lista):
        self.lista = lista 
        self.posicion = 0
        self.tipo = ""
        self.valor = ""
        self.fondo= ""
        self.valores =[]  
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

    def limpiar(self):
        self.tipo = ""
        self.valor = ""
        self.fondo= ""
        self.valores =[]  
        self.nombre =""
        self.evento = ""


    def escribir(self):
        if self.tipo == "etiqueta":
            self.resultado += "<div> <label> "+ self.valor + "</label> </div>\n"
            self.limpiar()
        elif self.tipo == "texto":
            self.resultado += ' <div> < input type="text" placeholder="'+self.fondo +'" > </div>\n' 
            self.limpiar()
        elif self.tipo == "grupo-radio":
            self.resultado += " <div> <p>" + self.nombre +":</p> </div>"
            if len(self.valores) > 0:
                for valor in self.valores:
                    self.resultado += '<div> <input type="radio" id="'+ valor +'" value="'+ valor +'"><label for="'+ valor +'">'+ valor +'</label></div>\n'
            else:    
                 self.resultado += '<div> <input type="radio" id="'+ self.valor +'" value="'+ self.valor +'"><label for="'+ self.valor +'">'+ self.valor +'</label></div>\n'
            self.limpiar()

        elif self.tipo == "grupo-option":
            self.resultado += '<div> <label for="'+ self.nombre +'">'+ self.nombre +':</label> <\div>\n'
            self.resultado += '<select name="'+ self.nombre +'" id="'+ self.nombre +'">'
            
            if len(self.valores) > 0:
                for valor in self.valores:
                    self.resultado += '<option value = "'+ valor +'">'+ valor +'</option>' 
            else:
                    self.resultado += '<option value = "'+ self.valor +'">'+ self.valor +'</option>'
            self.resultado += '</select>'
            self.limpiar()

        elif self.tipo == "boton":
            self.resultado  += '<div> <button type="button">'+self.valor+'</button><\div>\n'
            self.limpiar()







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
                    self.paraValores()
                    if self.aux.tipo == "]":
                        self.obtenerSiguiente()
                        if  self.aux.tipo == ",":
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
                    self.tiposDos()
                    if self.aux.tipo == ">":
                            self.obtenerSiguiente()
                            if self.aux.tipo == ",":
                                self.obtenerSiguiente()
                                self.elemento()
                            elif  self.aux.tipo == ">":
                                return
    
        elif self.aux.tipo == "nombre":
            self.obtenerSiguiente()
            if self.aux.tipo == ":":
                self.obtenerSiguiente()
                if self.aux.tipo == "texto":
                    self.nombre = self.aux.lexema
                    self.obtenerSiguiente()
                    if self.aux.tipo == ",":
                        self.obtenerSiguiente()
                        self.elemento()
                    
                    elif  self.aux.tipo == ">":
                            return



            
                
    def tipos(self):
        
        if self.aux.lexema == "etiqueta":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
        elif self.aux.lexema == "texto":
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
        
        if self.aux.lexema == "entrada":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
        elif self.aux.lexema == "info":
            self.tipo = self.aux.lexema
            self.obtenerSiguiente()
    
    def paraValores(self):

        if self.aux.tipo == "texto2":
            self.valores.append(self.aux.lexema)  
            self.obtenerSiguiente()
            if self.aux.tipo == ",":
                self.obtenerSiguiente()
                self.paraValores()
            elif self.aux.tipo == "]":
                return
                




                    

                        



