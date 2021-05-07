#problema: ingrese 3 notas de un estudiante y halle su promedio
#solucion
import math
#var de entrada
n1 = int(input("Ingrese Nota 1: "))
n2 = int(input("Ingrese Nota 2: "))
n3 = int(input("Ingrese Nota 3: "))
#var de operacion
prom = math.ceil ((n1 + n2 + n3)/3.0)
#var de salida
print("El promedio es:",prom)
