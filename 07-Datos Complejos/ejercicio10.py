#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Perú": "Lima"
}

invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
