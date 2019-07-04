
import pygame

class item:
    def __init__(self, name, icon):
        self.name = name
        self.x = 0
        self.y = 0
        self.icon = pygame.image.load(icon)
        self.icon = pygame.transform.scale(self.icon, (64, 64))

class room:
    def __init__(self, name, text, background):
        self.name = name
        self.text = text
        self.background = pygame.image.load(background)
        self.items = []
        self.directions = {}
    
    def add_adjacent_room(self, direction, r):
        self.directions.update({direction: r})

    def add_item(self, i, x, y):
        item.x = x
        item.y = y
        self.items.append(i)

    def remove_item(self, i):
        self.items.remove(i)
