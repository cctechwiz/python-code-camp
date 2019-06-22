"""
dict_adventure.py

A text adventure using a dictionary.

Credit: https://python-forum.io/Thread-Text-Adventure-Tutorial-if-structure-to-dictionary
"""
 
# data setup
rooms = {
    'empty': {
        'name': 'an empty room', 
        'east': 'bedroom', 
        'north': 'temple',
        'text': 'The stone floors and walls and cold and damp.'},
    'temple': {
        'name': 'a small temple', 
        'east': 'torture', 
        'south': 'empty',
        'text': 'There are three rows of benches facing a small statue.'},
    'torture': {
        'name': 'a torture chamber', 
        'west': 'temple', 
        'south': 'bedroom',
        'text': 'There is a rack and an iron maiden against the wall\nand some chains and thumbscrews on the floor.'},
    'bedroom': {
        'name': 'a bedroom', 
        'north': 'torture', 
        'west': 'empty',
        'text': 'There is a large bed with black, silk sheets on it.'}
    }
directions = ['north', 'south', 'east', 'west']
current_room = rooms['empty']
 
# game loop
while True:
    # display current location
    print()
    print('You are in {}.'.format(current_room['name']))
    print(current_room['text'])
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # bad command
    else:
        print("I don't understand that command.")