#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas = [5,10,8,9,6.5,7,4,2,9,6.25]
suma = 0

print(f"Las notas de los alumnos son: {notas}")

for i in notas:
    suma += i

promedio = float(suma / len(notas))

# Nota maxima y minima

nota_maxima = notas[0]
nota_minima = notas[0]

for i in notas:
    if i > nota_maxima:
        nota_maxima = i
    if i < nota_minima:
        nota_minima = i


print(f"El promedio de las notas es de: {promedio}")
print(f"La nota maxima fue de: {nota_maxima}")
print(f"La nota minima fue de: {nota_minima}")