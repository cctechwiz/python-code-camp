from npc import npc
from room import room

# Create rooms
empty = room('an empty room', 'The stone floors and walls are cold and damp.')
temple = room('a small temple', 'There are three rows of benches facing a small statue.')
torture = room('a torture chamber', 'There is a rack and an iron maiden against the wall\nand some chains and thumbscrews on the floor.')
bedroom = room('a bedroom', 'There is a large bed with black, silk sheets on it.')

# Create npcs
priest = npc('priest', 'a priestly figure in long white robes.')
priest.add_line('Hello child.')
priest.add_line('Welcome to the temple.')
priest.add_line('Please take all the time you need.')

maid = npc('maid', 'a short, plump lady with a feather duster in her hand.')
maid.add_line('Oh!')
maid.add_line('Please excuse the mess.')
maid.add_line("Sorry. I'm almost done.")

# Setup rooms
empty.add_adjacent_room('east', bedroom)
empty.add_adjacent_room('north', temple)

temple.add_adjacent_room('east', torture)
temple.add_adjacent_room('south', empty)
temple.add_item('bench')
temple.add_item('bench')
temple.add_item('bench')
temple.add_item('statue')
temple.add_npc(priest)
# TODO: Add crafting

torture.add_adjacent_room('west', temple)
torture.add_adjacent_room('south', bedroom)
torture.add_item('chains')
torture.add_item('thumbscrews')

bedroom.add_adjacent_room('north', torture)
bedroom.add_adjacent_room('west', empty)
bedroom.add_item('sheets')
bedroom.add_item('bed')
bedroom.add_npc(maid)

directions = ['north', 'south', 'east', 'west']
commands = ['quit', 'q',
            'help', 'h',
            'items', 'i',
            'look', 'l',
            'get', 'g',
            'drop', 'd',
            'talk', 't']

help_message = """
--- help ---
to look around type:
    'look'
to move type:
    'north', 'south', 'east', or 'west'
to see items you're holding:
    'items'
to pick up an item type:
    'get <item>'
to drop an item type:
    'drop <item>'
to talk to an npc type:
    'talk <npc>'
to quit type:
    'q' or 'quit' """

carrying = []

current_room = empty
current_room.print_room_info()
 
# game loop
while True:
    # get user input
    command = input('\nWhat do you do?\n> ').strip().lower()
    # movement commands
    if command in directions:
        if command in current_room.directions:
            current_room = current_room.directions[command]
            current_room.print_room_info()
        else:
            print("You can't go that way.")
    # other supported commands
    elif command.split()[0] in commands:
        cmd = command.split()[0]
        # quit the game
        if cmd in ('q', 'quit'):
            break
        # ask for help
        elif cmd in ('h', 'help'):
            print(help_message)
        # show items you're carrying
        elif cmd in ('i', 'items'):
            if carrying:
                print('You are carrying: {}'.format(', '.join(carrying)))
            else:
                print('You are not carrying anything')
        # look around the room
        elif cmd in ('look', 'l'):
            current_room.print_room_info()
        # pick up an object
        elif cmd in ('get', 'g'):
            if len(command.split()) == 1:
                print("What do you pick up?")
                continue
            item = command.split()[1]
            if item in current_room.items:
                current_room.remove_item(item)
                carrying.append(item)
            else:
                print("I don't see that here.")
        # drop an object
        elif cmd in ('drop', 'd'):
            # TODO: allow for items with spaces
            if len(command.split()) == 1:
                print("What do you drop?")
                continue
            item = command.split()[1]
            if item in carrying:
                carrying.remove(item)
                current_room.add_item(item)
            else:
                print("You aren't carrying that.")
        # talk to an npc
        elif cmd in ('talk', 't'):
            if len(command.split()) == 1:
                print("Who do you talk to?")
                continue
            npc = command.split()[1]
            if npc in current_room.npcs:
                current_room.npcs[npc].talk()
            else:
                print("You don't see anyone called that.")
    # bad command
    else:
        print("I don't understand that command.")
        print("   (You can ask for 'help')")