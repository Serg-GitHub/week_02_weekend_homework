from classes.guest import Guest
from classes.song import Song
class Rooms:
    def __init__(self, guest_list):
        self.guest_list = guest_list
        self.song_list = []
        
# Test to check in and check out guests passed.
    def guest_check_in(self, guest):
        for guest in guest:
           self.guest_list.append(guest)

    def guest_check_out(self, guest):
        for guest in guest: 
           self.guest_list.append(guest)       
                