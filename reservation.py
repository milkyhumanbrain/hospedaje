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

    while True:
        menu()
        opcion = input("\nElegir una opción del (1 - 6): ")

        if opcion == "1": 
            room = get_room_by_id(1)
            if room['disponibilidad'] > 0:
                dias = input("Ingrese los días a alojarse o escriba (cancelar) para salir del registro: ")
                if dias.lower() == "cancelar":
                    continue
                if dias.isdigit() and int(dias) > 0:
                    dias = int(dias)
                    total = dias * 80
                    print(f"\nReserva confirmada para {nombres.title()} con DNI {dni}")
                    print(f"Habitación Simple por {dias} días. Total: S/ {total}")
                    room['disponibilidad'] -= 1
                else:
                    print("Cantidad inválida.")
            else:
                print("No hay habitaciones simples disponibles.")

        elif opcion == "2":  
            room = get_room_by_id(2)
            if room['disponibilidad'] > 0:
                dias = input("Ingrese los días a alojarse o escriba (cancelar) para salir del registro: ")
                if dias.lower() == "cancelar":
                    continue
                if dias.isdigit() and int(dias) > 0:
                    dias = int(dias)
                    total = dias * 110
                    print(f"\nReserva confirmada para {nombres.title()} con DNI {dni}")
                    print(f"Habitación Doble por {dias} días. Total: S/ {total}")
                    room['disponibilidad'] -= 1
                else:
                    print("Cantidad inválida.")
            else:
                print("No hay habitaciones dobles disponibles.")

        elif opcion == "3": 
            room = get_room_by_id(3)
            if room['disponibilidad'] > 0:
                dias = input("Ingrese los días a alojarse o escriba (cancelar) para salir del registro: ")
                if dias.lower() == "cancelar":
                    continue
                if dias.isdigit() and int(dias) > 0:
                    dias = int(dias)
                    total = dias * 150
                    print(f"\nReserva confirmada para {nombres.title()} con DNI {dni}")
                    print(f"Habitación Matrimonial por {dias} días. Total: S/ {total}")
                    room['disponibilidad'] -= 1
                else:
                    print("Cantidad inválida.")
            else:
                print("No hay habitaciones matrimoniales disponibles.")

        elif opcion == "4":
            print("\nHabitaciones disponibles:")
            for room in get_rooms():
                print(f"- {room['nombre']}: {room['disponibilidad']} disponibles - S/ {room['precio']}")

        elif opcion == "5":
            print("\nRegistrando nuevo cliente...")
            if not registrar_cliente():
                continue  

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")
