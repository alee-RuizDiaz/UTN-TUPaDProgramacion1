#4) Dada una lista con valores repetidos:
# datos = [1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
datos_sin_duplicar = []

for i in datos:
    if i not in datos_sin_duplicar:
        datos_sin_duplicar.append(i)

print(f"Lista original: {datos}")
print(f"Lista sin duplicados: {datos_sin_duplicar}")