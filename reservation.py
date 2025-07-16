import datetime
from storage import get_rooms, get_clients, add_client, get_client_by_dni, get_room_by_id
from utils import clear_screen, print_space

def hacer_reserva():
    clear_screen()
    print("--- Nueva Reserva ---")
    dni = input("Ingrese el DNI del cliente: ")
    cliente = get_client_by_dni(dni)

    if not cliente:
        nombre = input("Cliente no encontrado. Ingrese su nombre: ")
        cliente = {'nombres': nombre, 'dni': dni}
        add_client(cliente)
        print_space()
        print("Cliente registrado exitosamente.")
        print_space()

    rooms = get_rooms()
    print_space()
    print_space()
    print("Habitaciones disponibles:")
    for room in rooms:
        print(f"ID: {room['id']} | Tipo: {room['nombre']} | Precio: S/ {room['precio']} | Disponibles: {room['disponibilidad']}")

    try:
        print_space()
        room_id = int(input("Ingrese el ID de la habitación a reservar: "))
        dias = int(input("¿Cuántos días se hospedará?: "))
    except ValueError:
        print_space()
        print("Entrada inválida. Debe ingresar números.")
        print_space()
        input("Presione Enter para continuar...")
        return

    room = get_room_by_id(room_id)

    if not room:
        print_space()
        print("ID de habitación no válido.")
        print_space()
        input("Presione Enter para continuar...")
        return
    if room['disponibilidad'] <= 0:
        print_space()
        print("Lo sentimos, no hay disponibilidad para esa habitación.")
        print_space()
        input("Presione Enter para continuar...")
        return

    costo_total = room['precio'] * dias
    room['disponibilidad'] -= 1

    clear_screen()
    print("--- Resumen de la Reserva ---")
    print(f"Reserva registrada con éxito a las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
    print(f"- Cliente: {cliente['nombres']} (DNI: {cliente['dni']})")
    print(f"- Habitación: {room['nombre']}")
    print(f"- Duración: {dias} días")
    print(f"- Costo Total: S/ {costo_total}")
    print_space()
    input("Presione Enter para regresar al menú principal...")

def consultar_clientes():
    clear_screen()
    print("--- Clientes Registrados ---")
    clientes = get_clients()
    if not clientes:
        print_space()
        print("No hay clientes registrados.")
        print_space()
    else:
        for cliente in clientes:
            print(f"- {cliente['nombres']} | DNI: {cliente['dni']}")
    print_space()
    input("Presione Enter para continuar...")

def consultar_habitaciones():
    clear_screen()
    print("--- Estado de las Habitaciones ---")
    for room in get_rooms():
        print(f"- {room['nombre']} | Precio: S/ {room['precio']} | Disponibilidad: {room['disponibilidad']}")
    print_space()
    input("Presione Enter para continuar...")
