import os

def print_space():
    print("\n")

def print_separator():
    print("--------------------------------")

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_main_header():
    print("SISTEMA DE RESERVAS EL MIRADOR")
    print_separator()

def print_login_header():
    print("BIENVENIDO AL SISTEMA DE RESERVAS EL MIRADOR")
    print_separator()

def print_access_denied_header():
    print("ACCESO DENEGADO - INTENTOS AGOTADOS")
    print_separator()

def press_enter_to_continue():
    input("Presione Enter para continuar...")