#Problema 3: leer un numero de tres digitos, halle la suma y producto de sus digitos

#SOLUCION
#variable de entrada
num = int(input("Ingrese Numero de 3 digitos:"))
#variables de operaciones
uni = int(num / 100)
dec = (int(num % 100)/10)
cen = num % 10
sd = (uni+ dec+ cen)
pd = (uni * dec * cen)
#varibles de salida
print(uni)
print(dec)
print(cen)
print("Suma de digitos:",sd)
print("Producto de digitos:",pd)
