#Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input(f'Escribir contanto {i+1}/5: ').capitalize()
    tel = input(f'Escribir telefono de {nombre}: ')
    contactos[f'{nombre}'] = tel

buscar_nombre = input('Buscar número de: ').capitalize()

if buscar_nombre in contactos.keys():
    print(f'El número de {buscar_nombre} es: {contactos[f'{buscar_nombre}']}')
else:
    print(f'No existe el contacto {buscar_nombre}.')