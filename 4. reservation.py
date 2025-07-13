def mostrar_disponibles():
    print("\nHabitaciones disponibles: ")
    for room in get_rooms():
        print(f"- {room['nombre']}: {room['disponibilidad']} disponibles - S/ {room['precio']}")

def registrar_cliente():
    while True:
        nombres = input("\nIngrese los nombres del cliente (o escriba 'cancelar' para salir): ")
        if nombres.lower() == "cancelar":
            return None, None

        dni = input("Ingrese el número de DNI del cliente: ")

        if not dni.isdigit():
            print("\nDNI inválido. Debe contener solo números.")
            continue

        if get_client_by_dni(dni):
            print("\nEste cliente ya está registrado. Intente con otro DNI.")
            continue

        add_client({'nombres': nombres, 'dni': dni})
        print(f"\nCliente {nombres.title()}, con DNI: {dni} registrado con éxito.")
        return nombres, dni

def reservar_habitacion(id_habitacion, nombres, dni):
    room = get_room_by_id(id_habitacion)
    if room['disponibilidad'] == 0:
        print(f"No hay habitaciones {room['nombre'].lower()} disponibles.")
        return

    dias = input("Ingrese los días a alojarse o escriba (cancelar) para salir del registro: ")
    if dias.lower() == "cancelar":
        return
    if not dias.isdigit() or int(dias) <= 0:
        print("Cantidad inválida.")
        return

    total = int(dias) * room['precio']
    room['disponibilidad'] -= 1
    print(f"\nReserva confirmada para {nombres.title()} con DNI: {dni}")
    print(f"Habitación {room['nombre']} por {dias} días. Total: S/ {total}")