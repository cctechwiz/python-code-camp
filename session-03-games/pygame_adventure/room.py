
import pygame

class room:
    def __init__(self, name, text, background):
        self.name = name
        self.text = text
        self.background = pygame.image.load(background).convert()
        self.items = []
        self.npcs = {}
        self.directions = {}
    
    def add_adjacent_room(self, direction, room):
        self.directions.update({direction: room})

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_npc(self, npc):
        self.npcs.update({npc.name: npc})
        
    def print_room_info(self):
        print('\n---')
        print('You are in {}.'.format(self.name))
        print(self.text)
        print('There are {} exit(s) from this room: {}'.format(len(self.directions), ', '.join(self.directions.keys())))
        if self.items:
            print('In the room are: {}'.format(', '.join(self.items)))
        if self.npcs:
            print('You are not alone here: {}'.format(', '.join(self.npcs.keys())))
