from storage import get_rooms

def main():
    print("Bienvenido al sistema de reservas de habitaciones")
    
    # Mostrar habitaciones disponibles
    rooms = get_rooms()
    print("Habitaciones disponibles:", len(rooms))

if __name__ == "__main__":
    main()
    
main()