#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Escribir un número entero: "))

if num == 0:
    digito = 1
else:
    digito = 0
    while num > 0:
        num //= 10
        digito += 1

print(f"La cantidad de digitos es: {digito}")

