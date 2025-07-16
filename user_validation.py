import getpass
from utils import clear_screen, print_login_header, print_access_denied_header, print_space

def usuario_validacion(usuario):
    return usuario == "admin"

def contrasena_validacion(contrasena):
    return contrasena == "123456"

def registro():
    intentos = 3
    while intentos > 0:
        clear_screen()
        print_login_header()
        print_space()
        user = input("Ingrese su usuario: ")
        print_space()
        contrasena = getpass.getpass("Ingrese su contraseña: ")

        if usuario_validacion(user) and contrasena_validacion(contrasena):
            print_space()
            print("Acceso concedido. ¡Bienvenido!")
            print_space()
            input("Presione Enter para continuar...")
            return True

        intentos -= 1
        if intentos > 0:
            print_space()
            print(f"Usuario o contraseña incorrectos. Le quedan {intentos} intento(s).")
            print_space()
            input("Presione Enter para continuar...")

    clear_screen()
    print_access_denied_header()
    print_space()
    input("Presione Enter para salir...")
    return False