#problema 2: hallar el volumen de un cilindro

#SOLUCION
import math
#Var de entrada
radio = float(input("Ingrese radio: "))
altura = float(input("Ingrese la altura:"))
#Var de operacion
vc = math.pi * math.pow(radio, 2) * altura
#Var de salida
print("Volumen del cilindro:",vc)