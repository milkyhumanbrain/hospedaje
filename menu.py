clientes = []
habitaciones = ["101 - Disponible", "102 - Ocupada", "103 - Disponible"]

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Reserva")
    print("2. Consulta de clientes")
    print("3. Consulta de Habitaciones")
    print("4. Salir")

def hacer_reserva():
    nombre = input("Ingrese el nombre del cliente: ")
    habitacion = input("Ingrese la habitación (ej. 101): ")
    reserva = f"{nombre} - Habitación {habitacion}"
    clientes.append(reserva)
    print(f"Reserva realizada: {reserva}")

def consultar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
    else:
        print("Clientes registrados:")
        for cliente in clientes:
            print(f"- {cliente}")

def consultar_habitaciones():
    print("Estado de habitaciones:")
    for hab in habitaciones:
        print(f"- {hab}")

# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        hacer_reserva()
    elif opcion == "2":
        consultar_clientes()
    elif opcion == "3":
        consultar_habitaciones()
    elif opcion == "4":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
