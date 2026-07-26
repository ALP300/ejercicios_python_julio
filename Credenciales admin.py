# Credenciales validas:
user_admin_correcto = "admin"
password_admin_correcta = "12345"

# Input de datos

user = input("Ingrese su nombre de usuario:")
password = input("Ingrese su contraseña:")
role = input("Ingrese su rol (admin, editor, visitante")

# Validacion de datos

if user == user_admin_correcto and password == password_admin_correcta:
    print("Acceso concedido")

    if role == "admin":
        print("Permisos de Admin:")
        print("Gestionar usuarios")
        print("Gestionar contenido")
        print("Ver Base de Datos")

    elif role == "editor":
        print("Gestion de Editor")
        print("Crear contenido")
        print("Editar contenido")
    elif role == "visitante":
        print("Ver contenido")
        print("Guardar contendido")
    else:
        print("Rol no valido")
else:
    print("Credenciales invalidas")


