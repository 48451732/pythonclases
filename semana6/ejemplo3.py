# Programa: Hallar el volumen de una esfera
# Formula: V = V = 4/3.π.r³

#SOLUCION
import math
#Var de entrada
radio = float(input("Ingrese radio: "))
#Var de operacion
ve = 4/3 * math.pi * math.pow(radio, 3)
#Var de salida
print("Volumen de la esfera:",ve)