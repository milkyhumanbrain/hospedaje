def usuario_validacion(usuario):
    return usuario == "admin"

def contrasena_validacion(contrasena):
    return contrasena == "123456"

def registro():
    user = input("\nIngrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario_validacion(user):
        if contrasena_validacion(contrasena):
            print("\nAcceso concedido. Bienvenido Pablo.")
            return True
        else:
            print("\nContraseña incorrecta.")
    else:
        print("\nUsuario incorrecto.")
    return False