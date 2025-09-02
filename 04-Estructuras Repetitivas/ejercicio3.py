#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Escribir un número: "))
num2 = int(input("Escribir otro número: "))
suma = 0

# Intercambio valores para que funcione el ciclo for
if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1 + 1, num2):
    suma += i

print(f"La suma de los números comprendidos entre {num1} y {num2} es igual a: {suma}")