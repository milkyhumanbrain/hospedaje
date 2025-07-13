def usuario_validacion(usuario):
    return usuario == "admin"

def contrasena_validacion(contrasena):
    return contrasena == "123456"

def registro():
    intentos = 3
    while intentos > 0:
        user = input("\nIngrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if usuario_validacion(user) and contrasena_validacion(contrasena):
            print("\nAcceso concedido. Bienvenido Pablo.")
            return True

        intentos -= 1
        print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s).")

    print("\nAcceso denegado. Se acabaron los intentos.")
    return False