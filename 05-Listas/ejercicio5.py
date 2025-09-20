#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

alumnos = ["alejandro", "pedro", "pepe", "agustin", "lola", "maria", "sofia", "juan"]

print("Lista de alumnos:")
print(alumnos)

accion = input("Deseas agregar un nuevo estudiante o eliminar uno existente? agregar/eliminar ").lower()

if accion == "agregar":
    nuevo = input("Ingresar nombre de nuevo estudiante: ").lower()
    print(f"Se agrego al estudiante {nuevo} a la lista.")
    alumnos.append(nuevo)
elif accion == "eliminar":
    eliminar = input("Ingresar el nombre del estudiante que desea eliminar de la lista: ").lower()
    alumnos.remove(eliminar)
    print(f"Se elimino al estudiante {eliminar} de la lista.")
else:
    print("Opción no valida")

print(f"La nueva lista de estudiantes es: {alumnos}")


