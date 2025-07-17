from utils import print_space, clear_screen, press_enter_to_continue

# reporte_diario.py
# Módulo desarrollado para generar un resumen básico del día en el sistema de reservas.
# Muestra el total de huéspedes registrados, habitaciones ocupadas por tipo,
# e ingresos totales generados. Útil para revisar el rendimiento diario del hospedaje.
def generar_reporte_diario(reservas):
    clear_screen()
    print("Resumen diario – Hospedaje El Mirador")
    print_space()

    total_huespedes = len(reservas)
    simples = 0
    dobles = 0
    matrimoniales = 0
    ingresos = 0

    for r in reservas:
        tipo = r["tipo_habitacion"]
        precio = r["precio"]
        ingresos += precio

        if tipo == "simple":
            simples += 1
        elif tipo == "doble":
            dobles += 1
        elif tipo == "matrimonial":
            matrimoniales += 1

    print("--- Resumen Diario ---")
    print_space()
    print("Total de huéspedes registrados:", total_huespedes)
    print("Habitaciones simples ocupadas:", simples)
    print("Habitaciones dobles ocupadas:", dobles)
    print("Habitaciones matrimoniales ocupadas:", matrimoniales)
    print("Ingreso total del día: S/ {:.2f}".format(ingresos))
    print_space()
    press_enter_to_continue()
