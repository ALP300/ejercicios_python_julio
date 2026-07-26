''' 
Genera la tabla de multiplicar del 1 al 12 para los números del 1 al 10. Imprime cada
tabla en bloques separados
'''
for numero in range(1,11): 
    print(f"Tabla del {numero}")

    for multiplicador in range(1, 13):
        print(f"{numero} * {multiplicador} = {numero * multiplicador}")

print()

