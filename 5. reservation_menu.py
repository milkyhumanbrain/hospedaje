def menu_reserva():
    nombres, dni = registrar_cliente()
    if not nombres:
        return

    while True:
        mostrar_menu()
        opcion = input("\nElegir una opción del (1 - 6): ")

        if opcion == "1":
            reservar_habitacion(1, nombres, dni)
        elif opcion == "2":
            reservar_habitacion(2, nombres, dni)
        elif opcion == "3":
            reservar_habitacion(3, nombres, dni)
        elif opcion == "4":
            mostrar_disponibles()
        elif opcion == "5":
            nuevos = registrar_cliente()
            if nuevos[0]:
                nombres, dni = nuevos
        elif opcion == "6":
            print("Saliendo del sistema... ")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")