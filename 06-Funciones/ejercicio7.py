#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
#restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mul = a * b
    div = a / b

    print(f"{a} + {b} es: {suma}")
    print(f"{a} - {b} es: {resta}")
    print(f"{a} x {b} es: {mul}")
    print(f"{a} : {b} es: {div}")

num1 = int(input("Escribir primer número: "))
num2 = int(input("Escribir segundo número: "))

operaciones_basicas(num1, num2)