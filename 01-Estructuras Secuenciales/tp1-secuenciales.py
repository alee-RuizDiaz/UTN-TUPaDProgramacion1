# Ejercicio 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

#print("Hola Mundo!")

# Ejercicio 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

#nombre = input("Escriba su nombre: ")

#print(f"Hola {nombre}!")

#Ejercicio 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

#nombre = input("Escriba su nombre: ")
#apellido = input("Escriba su apellido: ")
#edad = int(input("Escriba su edad: "))
#residencia = input("Escriba su pais de residencia: ")

#print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

#radio = float(input("Ingresar el radio de un circulo: "))
#pi = 3.14159
#area = pi * radio * radio
#perimetro = 2 * pi * radio

#print(f"Un circulo con un radio de {radio}, su área es de {area} y su perimetro es de {perimetro}")

#Ejercicio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

#segundos = int(input("Escribir la cantidad de segundos que quieras pasar a horas: "))
#minutos = segundos / 60
#horas = minutos / 60

#print(f"{segundos} equivale a {horas} horas.")

#Ejercicio 6
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

#numero = int(input("Escribir un numero: "))

#for i in range(1, 11):
#    resultado = numero * i
#    print(f"{numero} x {i} = {resultado}")

#Ejercicio 7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#num1 = int(input("Escribir primer numero: "))
#num2 = int(input("Escribir segundo numero: "))

#suma = num1 + num2
#resta = num1 - num2
#multiplicar = num1 * num2
#dividir = num1 / num2

#print(f"La suma de {num1} y {num2} es de: {suma}")
#print(f"La resta de {num1} y {num2} es de: {resta}")
#print(f"La multiplicación de {num1} y {num2} es de: {multiplicar}")
#print(f"La división de {num1} y {num2} es de: {dividir}")

#Ejercicio 8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

#peso = float(input("¿Cual es tu peso en Kg?"))
#altura = float(input("¿Cual es tu altura en metros?"))

#imc = peso / (altura ** 2)

#print(f"Su indice de masa corporal segun su peso y altura es de: {imc}")

#Ejercicio 9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit

#celsius = float(input("Ingrese la temperatura en grados celsius: "))

#fahrenheit = (celsius * 9/5) + 32

#print(f"{celsius}°C equivalen a {fahrenheit}°F")

#Ejercicio 10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

#num1 = float(input("Escribir primer numero: "))
#num2 = float(input("Escribir segundo numero: "))
#num3 = float(input("Escribir tercero numero: "))

#promedio = (num1 + num2 + num3) / 3

#print(f"El promedio de {num1}, {num2} y {num3} es de: {promedio}")

ruta = "C:\carpeta\notas.csv"
print(ruta)