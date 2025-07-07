# Data Pre-poblada
rooms = [
    {'precio': 100.0, 'nombre': 'Suite',     'disponibilidad': 5, 'id': 1},
    {'precio':  50.0, 'nombre': 'Standard',  'disponibilidad':10, 'id': 2},
    {'precio': 150.0, 'nombre': 'Deluxe',    'disponibilidad': 2, 'id': 3},
]

clients = [
    {'nombres': 'Juan Perez',  'dni': '12345678'},
    {'nombres': 'Maria Gomez', 'dni': '87654321'},
]

def get_rooms():
    return rooms

def get_clients():
    return clients

def add_client(client_dict):
    clients.append(client_dict)

def get_client_by_dni(dni):
    for client in clients:
        if client['dni'] == dni:
            return client
    return None

def get_room_by_id(id):
    for room in rooms:
        if room['id'] == id:
            return room
    return None