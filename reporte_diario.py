# reporte_diario.py
# Módulo desarrollado para generar un resumen básico del día en el sistema de reservas.
# Muestra el total de huéspedes registrados, habitaciones ocupadas por tipo,
# e ingresos totales generados. Útil para revisar el rendimiento diario del hospedaje.
def generar_reporte_diario(reservas):
    print("Resumen del día – Hospedaje El Mirador")
    print("--------------------------------------")

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

    print("Total de huéspedes registrados:", total_huespedes)
    print("Habitaciones simples ocupadas:", simples)
    print("Habitaciones dobles ocupadas:", dobles)
    print("Habitaciones matrimoniales ocupadas:", matrimoniales)
    print("Ingreso total del día: S/ {:.2f}".format(ingresos))
    print("Gracias por usar el sistema")
