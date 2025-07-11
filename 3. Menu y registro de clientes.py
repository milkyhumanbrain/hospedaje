def menu():
    print("\nMenú de habitaciones:")
    print("1. Habitación simple")
    print("2. Habitación doble")
    print("3. Habitación matrimonial")
    print("4. Ver habitaciones disponibles")
    print("5. Registrar nuevo cliente")
    print("6. Salir")

def menu_reserva():
    nombres = ""
    dni = ""

    def registrar_cliente():
        nonlocal nombres, dni
        nombres = input("\nIngrese los nombres del cliente: ")
        dni = input("Ingrese el número de DNI del cliente: ")

        if not dni.isdigit():
            print("DNI inválido.")
            return False

        if get_client_by_dni(dni):
            print("Este cliente ya está registrado. No se puede registrar nuevamente.")
            return False
        else:
            add_client({'nombres': nombres, 'dni': dni})
            print(f"\nCliente {nombres.title()} con DNI {dni} registrado con éxito.")
            return True

    if not registrar_cliente():
        return