class room:    
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.items = []
        self.directions = {}
    
    def add_adjacent_room(self, direction, room):
        self.directions.update({direction: room})

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
        
    def print_room_info(self):
        print('\n---')
        print('You are in {}.'.format(self.name))
        print(self.text)
        print('There are {} exit(s) from this room: {}'.format(len(self.directions), ', '.join(self.directions.keys())))
        if self.items:
            print('In the room are: {}'.format(', '.join(self.items)))


# Create rooms
empty = room('an empty room', 'The stone floors and walls are cold and damp.')
temple = room('a small temple', 'There are three rows of benches facing a small statue.')
torture = room('a torture chamber', 'There is a rack and an iron maiden against the wall\nand some chains and thumbscrews on the floor.')
bedroom = room('a bedroom', 'There is a large bed with black, silk sheets on it.')

# Setup rooms
empty.add_adjacent_room('east', bedroom)
empty.add_adjacent_room('north', temple)

temple.add_adjacent_room('east', torture)
temple.add_adjacent_room('south', empty)
temple.add_item('bench')
temple.add_item('bench')
temple.add_item('bench')
temple.add_item('statue')

torture.add_adjacent_room('west', temple)
torture.add_adjacent_room('south', bedroom)
torture.add_item('chains')
torture.add_item('thumbscrews')

bedroom.add_adjacent_room('north', torture)
bedroom.add_adjacent_room('west', empty)
bedroom.add_item('sheets')
bedroom.add_item('bed')

directions = ['north', 'south', 'east', 'west']
commands = ['quit', 'q', 'help', 'h', 'items', 'i', 'look', 'l']
help_message = """
--- help ---
to look around:
    type 'look'
to move:
    type a direction
to see items you're holding:
    type 'items'
to pick up an item:
    type 'get <item>'
to drop an item:
    type 'drop <item>'
to quit:
    type 'q' or 'quit' """

carrying = []

current_room = empty
current_room.print_room_info()
 
# game loop
while True:
    # get user input
    command = input('\nWhat do you do?\n> ').strip().lower()
    # movement
    if command in directions:
        if command in current_room.directions:
            current_room = current_room.directions[command]
            current_room.print_room_info()
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command in commands:
        if command in ('q', 'quit'):
            break
        elif command in ('h', 'help'):
            print(help_message)
        elif command in ('i', 'items'):
            if carrying:
                print('You are carrying: {}'.format(', '.join(carrying)))
            else:
                print('You are not carrying anything')
        elif command in ('look', 'l'):
            current_room.print_room_info()
    # gather objects
    elif command.split()[0] == 'get':
        item = command.split()[1]
        if item in current_room.items:
            current_room.remove_item(item)
            carrying.append(item)
        else:
            print("I don't see that here.")
    # get rid of objects
    elif command.split()[0] == 'drop':
        item = command.split()[1]
        if item in carrying:
            carrying.remove(item)
            current_room.add_item(item)
        else:
            print("You aren't carrying that.")
    # bad command
    else:
        print("I don't understand that command.")
        print('--- (You can ask for \'help\') ---')