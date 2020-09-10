from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "This room contains - 'Lantern'",
                     "Lantern"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
"This room contains - 'Sword'",
"Sword"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
"This room contains - 'nothing...'",
"Nothing..."),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
"This room contains - 'A piece of blank paper?'",
"Blank paper"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
"This room contains - 'Not treasure...'",
'Not treasure'),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Kyle', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def getItem():
    y = input(f'Pick up {player1.location.items}? "y" or "n" ')
    print(y)
    if y == "y":
        print('You picked up item!')
        player1.items.insert(1, player1.location.items)
        print(f"You now have {player1.location.items}")
        print('You continue onward')
    else:
        print("You continue onward")

def dropItem():
    print(f"Your {player1.items} disappears into oblivion")
    player1.items.pop(0)


while True:
    print(player1.location.name)
    print(player1.location.description)

    x = input('Enter "n" "s" "e" "w" press "l" to look around press "d" to drop current item press "i" to show current inventory or press "q" to quit: ')
    try:
        if x == "n":
            player1.location = player1.location.n_to
        elif x == "s":
            player1.location = player1.location.s_to
        elif x == "e":
            player1.location = player1.location.e_to
        elif x == "w":
            player1.location = player1.location.w_to
        elif x == "l":
            print(player1.location.item_desc)
            getItem()
        elif x == "d":
            dropItem()
        elif x == "i":
            if player1.items == []:
                print("You haven't picked anything up yet!")
            else:
                print(player1.items)
        elif x == "q":
            print("quit!")
            break
    except: 
        print("You can't do that!")