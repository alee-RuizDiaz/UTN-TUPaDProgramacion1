#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

num = int(input("Escribir un número entero: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Escribir un número entero: "))

print("La suma de los números es de :", suma)