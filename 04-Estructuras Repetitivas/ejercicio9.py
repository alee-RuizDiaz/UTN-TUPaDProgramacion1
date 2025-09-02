#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#Se puede cambiar por 100 para cumplir con el enunciado
cantidad = 5 
suma = 0  

for i in range(cantidad):
    num = int(input(f"Ingresar número {i+1} de {cantidad}: "))
    suma += num

media = suma / cantidad

print(f"La media de los {cantidad} números ingresados es: {media}")
