'''
Sistema de clasificación de rendimiento: 
Solicita al usuario su nota (0-20) y su asistencia (%). Si la nota es mayor o igual a 11 y 
la asistencia es mayor o igual al 70%, se aprueba. De lo contrario, se desaprueba. 
'''
nota= int(input("Ingrese su nota: "))
asistencia= int(input("Ingrese su asistencia: "))
if nota >= 11 and asistencia >= 70:
    print("Aprobado")
else:
    print("Desaprobado")