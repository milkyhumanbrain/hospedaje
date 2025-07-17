from utils import clear_screen, print_space, press_enter_to_continue
from storage import get_rooms, get_clients

# Function to display all registered clients
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
    press_enter_to_continue()

# Function to display all available rooms
def consultar_habitaciones():
    clear_screen()
    print("--- Estado de las Habitaciones ---")
    for room in get_rooms():
        print(f"- {room['nombre']} | Precio: S/ {room['precio']} | Disponibilidad: {room['disponibilidad']}")
    print_space()
    press_enter_to_continue()