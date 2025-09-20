#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.


notas = [
    [7, 8, 9],  # Estudiante 1
    [9, 5, 8],  # Estudiante 2
    [6, 7, 7],  # Estudiante 3
    [8, 9, 4],  # Estudiante 4
    [5, 6, 7]   # Estudiante 5
]

#Mostramos las notas de los estudiantes
print("Notas de los estudiantes (materias 1,2,3):")

for i, estudiante in enumerate(notas, start=1):
    print(f"Estudiante {i}: {estudiante}")

print("")

# Promedio por estudiante
print("Promedio por estudiante:")

for i, estudiante in enumerate(notas, start=1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio:.2f}")

print("")

# Promedio por materia
print("Promedio por materia:")

num_materias = len(notas[0])

for materia in range(num_materias):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][materia]
    promedio_materia = suma_materia / len(notas)
    print(f"Materia {materia+1}: {promedio_materia:.2f}")
