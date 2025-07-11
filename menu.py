from storage import get_rooms, get_clients, add_client, get_client_by_dni, get_room_by_id
import datetime

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Reserva")
    print("2. Consulta de clientes")
    print("3. Consulta de Habitaciones")
    print("4. Salir")

def hacer_reserva():
    dni = input("Ingrese el DNI del cliente: ")
    cliente = get_client_by_dni(dni)

    if not cliente:
        nombre = input("Cliente no encontrado. Ingrese su nombre: ")
        cliente = {'nombres': nombre, 'dni': dni}
        add_client(cliente)
        print("Cliente registrado exitosamente.")

    # Mostrar habitaciones
    rooms = get_rooms()
    print("\nHabitaciones disponibles:")
    for room in rooms:
        print(f"ID: {room['id']} | Tipo: {room['nombre']} | Precio: S/ {room['precio']} | Disponibles: {room['disponibilidad']}")

    try:
        room_id = int(input("Ingrese el ID de la habitación a reservar: "))
        dias = int(input("¿Cuántos días se hospedará?: "))
    except ValueError:
        print("Entrada inválida. Debe ingresar números.")
        return

    room = get_room_by_id(room_id)

    if not room:
        print("ID de habitación no válido.")
        return
    if room['disponibilidad'] <= 0:
        print("Lo sentimos, no hay disponibilidad para esa habitación.")
        return

    costo_unitario = room['precio']
    costo_total = costo_unitario * dias
    hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Reducir la disponibilidad en 1
    room['disponibilidad'] -= 1

    # Mostrar resumen
    print("\nReserva registrada con éxito. Detalles:")
    print(f"- Cliente: {cliente['nombres']}")
    print(f"- DNI: {cliente['dni']}")
    print(f"- Hora actual: {hora_actual}")
    print(f"- Tipo de habitación: {room['nombre']}")
    print(f"- Costo unitario por noche: S/ {costo_unitario}")
    print(f"- Total por {dias} días: S/ {costo_total}")

    input("\nPresione Enter para regresar al menú principal...")

def consultar_clientes():
    print("\nClientes registrados:")
    for cliente in get_clients():
        print(f"- {cliente['nombres']} | DNI: {cliente['dni']}")

def consultar_habitaciones():
    print("\nEstado de habitaciones:")
    for room in get_rooms():
        print(f"- {room['nombre']} | Precio: S/ {room['precio']} | Disponibilidad: {room['disponibilidad']}")

def main():
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

if __name__ == "__main__":
    main()

