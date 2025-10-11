agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio",
    ("jueves", "07:00"): "Ir a la oficina",
    ("viernes", "20:30"): "Natación"
}

# Mostrar la agenda actual
print("Agenda actual:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia.capitalize()} a las {hora}: {evento}")


dia_consulta = input("\nIngresá el día que querés consultar: ").lower()
hora_consulta = input("Ingresá la hora (por ejemplo 10:00): ")

clave = (dia_consulta, hora_consulta)

if clave in agenda:
    print(f"\nEl {dia_consulta} a las {hora_consulta} hay: {agenda[clave]}")
else:
    print(f"\nNo hay actividades registradas el {dia_consulta} a las {hora_consulta}.")
