#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Escribir tu nombre: ")
apellido = input ("Escribir tu apellido: ")
edad = input("Escribir tu edad: ")
residencia = input("En que pais vives? ")

informacion_personal(nombre, apellido, edad, residencia)