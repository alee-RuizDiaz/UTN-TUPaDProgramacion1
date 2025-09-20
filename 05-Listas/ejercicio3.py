#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

import random

lista_azar = []

for i in range(1,16):
    lista_azar.append(random.randint(1, 100))

print("La lista con 15 números al azar:")
print(lista_azar)
print("")

lista_par = [i for i in lista_azar if i % 2 == 0]
lista_impar = [i for i in lista_azar if i % 2 != 0]

print(f"Lista con números par: {lista_par}")
print(f"Posee un total de {len(lista_par)} números")
print("")
print(f"Lista con números impar: {lista_impar}")
print(f"Posee un total de {len(lista_impar)} números")
