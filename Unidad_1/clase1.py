class coche:
    #inicialización
    def __init__(self, marca, modelo, color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.velocidad=0

    #métodos
    def acelerar(self,valor):
        self.velocidad += valor

    def frenar(self,valor):
        self.velocidad -= valor
    
    def getVelocidad(self):
        return self.velocidad

#función del programa principal     
def main():
    coche1= coche("peugeot","306","azul") 
    coche2=coche("seat","ibiza","blanco")

    coche1.acelerar(50)
    coche2.acelerar(130)
    
    print("----El coche 1 va a " , coche1.getVelocidad())
    print("----El coche 2 va a " , coche2.getVelocidad())

    coche2.frenar(40)
    print("-----El coche 2 va a " , coche2.getVelocidad())

#truco para poder ejecutar directamente la clase para probarla
if __name__ == "__main__":
    main()
