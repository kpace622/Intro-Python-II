# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    @classmethod
    def pickUpItem(cls):
        print("you picked up item!")
        
    def __str__(self):
        return f"{self.current_room}"
