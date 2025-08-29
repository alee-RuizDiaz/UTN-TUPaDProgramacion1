#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("En que hemisferio estas? Norte o Sur: ").title()
dia = int(input("En que día del mes estas? (escribir el número): "))
mes = int(input("En que mes estas? (escribir el mes del 1 al 12): "))

if hemisferio == "Norte":
    if (mes >= 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Estás en Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Estas en Primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Estas en Verano")
    else:
        print("Estas en Otoño")
elif hemisferio == "Sur":
    if (mes >= 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Estás en Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Estas en Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Estas en Inverno")
    else:
        print("Estas en Primavera")
else:
    print("Hemisferio invalido")