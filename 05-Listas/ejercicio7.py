#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

matriz = [
    [1, 10],  # Dia 1
    [2, 12],  # Dia 2
    [3, 11],  # Dia 3
    [8, 20],  # Dia 4
    [4, 13],  # Dia 5
    [6, 17],  # Dia 6
    [9, 19]   # Dia 7
]

print("Temperatura de la semana con minimos y maximos: ")
for i, dia in enumerate(matriz, start=1):
    print(f"Día {i}: Min={dia[0]}°, Max={dia[1]}°")

# calculamos promedio de min y max

suma_min = 0
suma_max = 0

for dia in matriz:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min / len(matriz)
promedio_max = suma_max / len (matriz)

print(f"El promedio de las temperaturas minimas es de: {promedio_min:.2f}°")
print(f"El promedio de las temperaturas maximas es de: {promedio_max:.2f}°")

#Buscamos el día con mayor amplitud termica (diferencia entre la minima y la maxima)
temp_mayor = 0
dia_temp_mayor = 0

for i, dia in enumerate(matriz):
    amplitud = dia[1] - dia[0]
    if amplitud > temp_mayor:
        temp_mayor = amplitud
        dia_temp_mayor = i + 1

print(f"El día con mayor amplitud termica fue el día {dia_temp_mayor} con {temp_mayor}°")



