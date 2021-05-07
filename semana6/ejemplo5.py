a = 10
b = 3
c = a / b
r = a % b #resto/mod/modulo
print(c)
print(r)


#problema: leer un numero entero de 2 digitos y muetralo al reves
#ejemplo: 21 --> 12

#SOLUCION
#variable de entrada
num = int(input("Ingrese Numero de 2 digitos:"))
#variables de operaciones
uni = int(num / 10)
dec = num % 10
ni = dec * 10 + uni
#varibles de salida
print(uni)
print(dec)
print("Numero invertido:",ni)