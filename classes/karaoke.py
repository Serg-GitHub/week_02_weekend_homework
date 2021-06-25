class Karaoke:
    def __init__(self, name):
        self.name = name
        self.room = []
    
    def room_count(self):
        return len(self.room)

    
    def add_room(self, room):
        self.room.append(room)
        