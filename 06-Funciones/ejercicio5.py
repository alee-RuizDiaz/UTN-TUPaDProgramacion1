#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Escribir segundos para pasar a horas: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")