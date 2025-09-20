#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista

productos = []

for i in range(0,5):
    productos.append(input(f"Ingresar el nombre de producto {i + 1}/5: "))

print(f"Lista de productos ingresados: {sorted(productos)}")

product_eliminado = input("Escribe el nombre de un producto para eliminarlo: ")
productos.remove(product_eliminado)

print(f"Usted elimino el producto {product_eliminado}, su lista de producto ahora es:")
print(sorted(productos))

