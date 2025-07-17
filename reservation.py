import datetime
from storage import get_rooms, get_clients, add_client, get_client_by_dni, get_room_by_id, add_reservation
from utils import clear_screen, print_space, press_enter_to_continue

def _get_or_create_client():
    dni = input("Ingrese el DNI del cliente: ")
    cliente = get_client_by_dni(dni)

    if not cliente:
        nombre = input("Cliente no encontrado. Ingrese su nombre: ")
        cliente = {'nombres': nombre, 'dni': dni}
        add_client(cliente)
        print_space()
        print("Cliente registrado exitosamente.")
        print_space()
    else:
        print_space()
        print(f"Cliente encontrado. {cliente['nombres']} ({cliente['dni']})")
        print_space()
    return cliente

def _select_room_and_days():
    rooms = get_rooms()
    print_space()
    print("Habitaciones disponibles:")
    for room in rooms:
        print(f"ID: {room['id']} | Tipo: {room['nombre']} | Precio: S/ {room['precio']} | Disponibles: {room['disponibilidad']}")
    print_space()

    try:
        room_id = int(input("Ingrese el ID de la habitación a reservar: "))
        dias = int(input("¿Cuántos días se hospedará?: "))
        return get_room_by_id(room_id), dias
    except ValueError:
        print_space()
        print("Entrada inválida. Debe ingresar números.")
        press_enter_to_continue()
        return None, None

def _confirm_and_process_reservation(cliente, room, dias):
    costo_total = room['precio'] * dias
    # We reduce the availability of the room by 1
    room['disponibilidad'] -= 1
    reserva_info = {
        'tipo_habitacion': room['nombre'].lower(),
        'precio': costo_total
    }
    add_reservation(reserva_info)

    clear_screen()
    print("--- Resumen de la Reserva ---")
    print(f"Reserva registrada con éxito a las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
    print(f"- Cliente: {cliente['nombres']} (DNI: {cliente['dni']})")
    print(f"- Habitación: {room['nombre']}")
    print(f"- Duración: {dias} días")
    print(f"- Costo Total: S/ {costo_total}")
    print_space()
    input("Presione Enter para regresar al menú principal...")

# Main function to handle the reservation process
def hacer_reserva():
    clear_screen()
    print("--- Nueva Reserva ---")
    print_space()

    cliente = _get_or_create_client()
    room, dias = _select_room_and_days()

    if not room or dias is None:
        print_space()
        print("ID de habitación no válido o entrada incorrecta.")
        print_space()
        press_enter_to_continue()
        return

    if room['disponibilidad'] <= 0:
        print_space()
        print("Lo sentimos, no hay disponibilidad para esa habitación.")
        print_space()
        press_enter_to_continue()
        return

    _confirm_and_process_reservation(cliente, room, dias)
