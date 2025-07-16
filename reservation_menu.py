from reservation import hacer_reserva, consultar_clientes, consultar_habitaciones
from menu import mostrar_menu
from utils import clear_screen, print_main_header, print_space

def menu_reserva():
    while True:
        clear_screen()
        print_main_header()
        mostrar_menu()
        print_space()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            hacer_reserva()
        elif opcion == "2":
            consultar_clientes()
        elif opcion == "3":
            consultar_habitaciones()
        elif opcion == "4":
            break
        else:
            print_space()
            print("Opción no válida. Intente nuevamente.")
            print_space()
            input("Presione Enter para continuar...")
