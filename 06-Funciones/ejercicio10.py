#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio entre {a}, {b}, {c} es: {promedio:.2f}")

num1 = float(input("Ingresar primer número: "))
num2 = float(input("Ingresar segundo número: "))
num3 = float(input("Ingresar tecer número: "))

calcular_promedio(num1, num2, num3)


