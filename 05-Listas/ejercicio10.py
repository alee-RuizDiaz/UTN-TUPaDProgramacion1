#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana

#Las dilas son los productos (4) y las columnas son las ventas por día
ventas = [
    [3, 4, 10, 15, 25, 1, 8],    # Producto 1
    [2, 15, 22, 31, 80, 1, 2],   # Producto 2
    [60, 5, 43, 34, 22, 15, 10], # Producto 3
    [17, 28, 31, 4, 52, 66, 7]   # Producto 4
]

print("Total vendido por cada producto:")
total_vendido = []
for i in range (4):
    total = sum(ventas[i])
    total_vendido.append(total)
    print(f"Producto {i+1}: {total}")

#Total vendido por dío
totales_dia = []
for dia in range(7):
    total_dia = 0
    for i in range (4):
        total_dia += ventas[i][dia]
    totales_dia.append(total_dia)

print("")

#Día con mayor ventas
max_ventas_dia = max(totales_dia)
dia_mayor_venta = totales_dia.index(max_ventas_dia) + 1
print(f"El día con mayores ventas totales fue el día {dia_mayor_venta} con {max_ventas_dia} ventas")

#Producto más vendido en la semana
max_ventas_producto = max(total_vendido)
producto_mas_vendido = total_vendido.index(max_ventas_producto) + 1
print(f"El producto más vendido en la semana fue el producto {producto_mas_vendido} con {max_ventas_producto} ventas")