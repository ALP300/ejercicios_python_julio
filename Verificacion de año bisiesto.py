'''
 Pide el año de nacimiento y determina si es bisiesto. Luego calcula la edad del usuario
 y verifica si es mayor de edad (18+).
'''
# Input de fecha de nacimiento
año_de_nacimiento = int(input("Ingrese su fecha de nacimiento: "))

año_actual = 2026    # Definiendo año actual. 
edad_usuario = año_actual - año_de_nacimiento   # Operacion simple para calcular edad actual
print(f"Tienes {edad_usuario} años.")

# Lógica para saber si el año es bisiesto
if (año_de_nacimiento % 4 == 0 and año_de_nacimiento % 100 != 0) or (año_de_nacimiento % 400 == 0):
    es_bisiesto = True
else:
    es_bisiesto = False

if es_bisiesto:
    print("Naciste en un año bisiesto.")
else:
    print("No naciste en un año bisiesto.")

#  Lógica para verificar si es mayor de edad
if edad_usuario >= 18:
    es_mayor = True
else:
    es_mayor = False

if es_mayor:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    


