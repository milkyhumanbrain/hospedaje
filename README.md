# Sistema de Reservas El Mirador

Este es un sistema simple para gestionar reservas de hotel desde la consola. Permite iniciar sesión, hacer reservas, registrar nuevos clientes y consultar la información de clientes y habitaciones.

## ¿Cómo funciona?

1. **Inicio de Sesión**: Al iniciar, se pide un usuario y contraseña. Por defecto, el usuario es "admin" y la contraseña es "123456".
2. **Menú Principal**: Una vez dentro, verás un menú con estas opciones:
   - Hacer una reserva.
   - Consultar clientes.
   - Consultar habitaciones.
   - Salir.
3. **Hacer una Reserva**:
   - El sistema te pide el DNI del cliente.
   - Si el cliente no existe, te pide su nombre para registrarlo al momento.
   - Luego, te muestra las habitaciones disponibles.
   - Eliges una habitación y cuántos días te quedarás.
   - Al final, te muestra un resumen de la reserva con el costo total.

## ¿Cómo ejecutar el programa?

Desde la terminal, en la carpeta del proyecto, usa este comando:

```bash

python3 main.py

```

## Estructura del Proyecto

El código está organizado en varios archivos:

- `main.py`: Inicia el programa.
- `user_validation.py`: Se encarga del login.
- `reservation_menu.py`: Controla el menú principal.
- `menu.py`: Muestra las opciones del menú.
- `reservation.py`: Contiene la lógica para hacer reservas y consultas.
- `storage.py`: Guarda los datos de las habitaciones y clientes.
- `utils.py`: Contiene funciones de ayuda para limpiar la pantalla y mostrar títulos.
