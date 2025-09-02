#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num = int(input("Adivina el número entre 0 y 9: "))
numeroAleatorio = random.randint(0, 9)
intentos = 1

while num != numeroAleatorio:
    intentos += 1
    print("Incorrecto. Intenta devuelta")
    num = int(input("Adivina el número entre 0 y 9: "))

print(f"Felicitaciones, el número era el {numeroAleatorio}, acertaste en el intento número {intentos}")