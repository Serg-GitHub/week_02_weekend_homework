import unittest
from classes.rooms import Rooms
from classes.guest import Guest
from classes.song import Song

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room = Rooms(1)
        self.guest = Guest("John Harper",[3])
        self.song = Song("Children", "Robert Miles", "Electronic")
        

    def test_room_has_guest_list(self):
        self.assertEqual(1,self.room.guest_list)    