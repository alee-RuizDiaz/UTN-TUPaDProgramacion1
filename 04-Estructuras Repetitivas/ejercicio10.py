#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingresar un número: "))
num_invertido = 0

while num > 0:
    digito = num % 10
    num_invertido = num_invertido * 10 + digito
    num = num // 10

print(f"El número invertido es: {num_invertido}")