#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


# Estudiantes aprobados
parcial1 = {"Ale", "Juan", "Eliana", "Jorge"}
parcial2 = {"Ale", "Pedro", "Luis", "Eliana"}

# Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos uno
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)
