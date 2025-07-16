from user_validation import registro
from reservation_menu import menu_reserva
from utils import print_space

def main():
    if registro():
        menu_reserva()
    print_space()
    print("Gracias por usar nuestro programa. ¡Hasta pronto!")
    print_space()

if __name__ == "__main__":
    main()