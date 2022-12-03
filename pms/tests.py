from django.test import TestCase, Client
from .models import Room, Room_type

class RoomTestCase(TestCase):
    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/6.0')
        self.roomtype_simple = Room_type.objects.create(name = "Simple",price = 20,max_guests = 1)
        self.roomtype_doble = Room_type.objects.create(name = "Doble",price = 30,max_guests = 2)
        self.roomtype_triple = Room_type.objects.create(name = "Triple",price = 40,max_guests = 3)
        self.roomtype_cuadruple = Room_type.objects.create(name = "Cuadruple",price = 50,max_guests = 4)

        self.room_simple_1 = Room.objects.create(room_type = self.roomtype_simple,name = "Room 1.1",description = "Disponible")
        self.room_simple_2 = Room.objects.create(room_type = self.roomtype_simple,name = "Room 1.2",description = "Disponible")
        self.room_doble = Room.objects.create(room_type = self.roomtype_doble,name = "Room 2.1",description = "Disponible")
        self.room_triple = Room.objects.create(room_type = self.roomtype_triple,name = "Room 3.1",description = "Disponible")
        self.room_cuadruple = Room.objects.create(room_type = self.roomtype_cuadruple,name = "Room 4.1",description = "Disponible")
    
    def test_search_room(self):
        response_0 = self.client.get('/rooms/')
        rooms_0 = list(response_0.context['rooms'].values())
        names_0 = [room['name'] for room in rooms_0]

        response_1 = self.client.get('/rooms/?name=Room+1')
        rooms_1 = list(response_1.context['rooms'].values())
        names_1 = [room['name'] for room in rooms_1]

        response_2 = self.client.get('/rooms/?name=Room+2')
        rooms_2 = list(response_1.context['rooms'].values())
        names_2 = [room['name'] for room in rooms_2]

        self.assertEqual(response_0.status_code, 200)
        self.assertEqual(names_0,['Room 1.1', 'Room 1.2', 'Room 2.1', 'Room 3.1', 'Room 4.1'])
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(names_1,['Room 1.1', 'Room 1.2'])
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(names_2,['Room 2.1'])
