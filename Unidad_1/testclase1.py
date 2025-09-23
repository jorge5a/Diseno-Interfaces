#import clase1
from clase1 import coche


coche1= coche("peugeot","306","azul")
coche2=coche("seat","ibiza","blanco")

coche1.acelerar(50)
coche2.acelerar(130)
    
print("El coche 1 va a " , coche1.getVelocidad())
print("El coche 2 va a " , coche2.getVelocidad())

coche2.frenar(40)
print("El coche 2 va a " , coche2.getVelocidad())
