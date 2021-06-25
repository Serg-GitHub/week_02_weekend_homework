import unittest
# from classes.song import Song
# from classes.karaoke import Karaoke
from classes.guest import Guest
from classes.rooms import Rooms

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Harper", "Children")


    def test_guest_has_name(self):
        self.assertEqual("John Harper", self.guest.name)


        

    
