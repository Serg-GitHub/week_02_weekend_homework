import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Children", "Robert Miles", "Electronic")
    
    def test_song_has_title(self):
        self.assertEqual("Children", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Robert Miles", self.song.artist)

    def test_song_has_type(self):
        self.assertEqual("Electronic", self.song.genre)









# import unittest
# from classes.guest import Guest
# from classes.karaoke import Karaoke
# from classes.rooms import Rooms
# from classes.song import Song 

# class TestSong(unittest.TestCase):
    
    