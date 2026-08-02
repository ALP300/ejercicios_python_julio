'''
Pide nombre, precio y categoría (tecnología, alimentos, ropa). Dependiendo de la
categoría y precio, aplica diferentes tipos de impuestos y clasificaciones (lujo, básico,
etc.
'''
# Datos a pedir con input
nombre = input("Ingrese el nombre del producto:")
precio = float(input("Ingrese el precio del producto:"))
categoria = input("Ingrese la categoría del producto (Tecnología, Alimentos o Ropa):").lower().strip()

# Determinar la clasificacion
if precio > 1000:
    clasificacion = "Lujo"
else:
    clasificacion = "Básico"

# Determinar el porcentaje de impuesto segun categoria y precio
if categoria == "alimentos":
    porcentaje_impuesto = 0.04  # 4%
elif categoria == "ropa":
    porcentaje_impuesto = 0.10  # 10%
elif categoria == "tecnología" or categoria == "tecnologia":
    if precio > 1000:
        porcentaje_impuesto = 0.21  # 21% (Impuesto para Tecnologia - Lujo)
    else:
        porcentaje_impuesto = 0.16  # 16% (Impuesto para Tecnologia - Basica)
else:
    porcentaje_impuesto = 0.15  # Impuesto para cualquier otra categoria

# Calculo de precios
monto_impuesto = precio * porcentaje_impuesto
precio_total = precio + monto_impuesto

# Prints
print("--- RESUMEN DEL PRODUCTO ---")
print(f"Producto: {nombre.capitalize()}")
print(f"Categoría: {categoria.capitalize()}")  # .capitalize() indica que la primera letra sea en mayuscula
print(f"Clasificación: {clasificacion}")
print(f"Precio Base: ${precio:.2f}")  # 2f indica que el numero se muestre con 2 decimales en float
print(f"Impuesto Aplicado ({porcentaje_impuesto * 100:.0f}%): ${monto_impuesto:.2f}")
print(f"Precio Total Final: ${precio_total:.2f}")



