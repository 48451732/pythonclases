#problemas de geometria basica
#hallar la longitud y el area de la circunferencia

#SOL
#var de entrada
import math
radio = float(input("Ingrese Radio: "))
#calculos
longitud = 2 * math.pi * radio
area = math.pi * math.pow(radio,2)
print("Longitud de la Circunferencia:",longitud)
print("Area de la Circunferencia:",area)