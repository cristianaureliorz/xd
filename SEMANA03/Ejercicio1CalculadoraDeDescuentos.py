def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

# Pedir datos al usuario
precio_original = float(input("Ingresa el precio del producto: S/"))
porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: %"))

# Llamar a la funcion y calcular el ahorro
precio_final = calcular_descuento(precio_original, porcentaje_descuento)
ahorro = precio_original - precio_final

#Mostramos los resultados
print(f"\nPrecio original: S/{precio_original}")
print(f"Precio final: S/{precio_final}")
print(f"Ahorro obtenido: S/{ahorro}")