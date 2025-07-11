rooms = [
    {'precio': 80.0, 'nombre': 'Simple', 'disponibilidad': 10, 'id': 1},
    {'precio': 110.0, 'nombre': 'Doble', 'disponibilidad': 20, 'id': 2},
    {'precio': 150.0, 'nombre': 'Matrimonial', 'disponibilidad': 5, 'id': 3},
]

clients = []

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