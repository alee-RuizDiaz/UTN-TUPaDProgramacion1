#Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe

stock = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}


print("Stock actual:", stock)

producto = input("\nIngresá el nombre del producto: ").lower()

if producto in stock:

    print(f"El producto '{producto}' tiene {stock[producto]} unidades en stock.")
    agregar = input("¿Querés agregar unidades? (s/n): ").lower()

    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad
        print(f"Stock actualizado de {producto}: {stock[producto]}")
    else:
        print("No se realizaron cambios.")

else:

    print(f"El producto '{producto}' no existe en el stock.")
    agregar_nuevo = input("¿Querés agregarlo? (s/n): ").lower()

    if agregar_nuevo == "s":
        cantidad = int(input("Ingresá la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agregó el producto.")

print("\nStock final:", stock)
