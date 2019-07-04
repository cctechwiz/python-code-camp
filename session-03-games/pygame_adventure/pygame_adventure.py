"""
Pygame version of adventure game
"""

import pygame

from room import room
from room import item

pygame.init()

screen_height = 800
screen_width = 800
screen_size = (screen_height, screen_width)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pygame Adventure')
clock = pygame.time.Clock()
game_running = True

player = pygame.image.load('./images/player.png')
player = pygame.transform.scale(player, (200, 200))
player_height = 180
player_width = 140

x = (screen_width * 0.40)
y = (screen_height * 0.40)
x_change = 0
y_change = 0

right_edge = screen_width - player_width
left_edge = -30
bottom_edge = screen_height - player_height
top_edge = -30

# Create rooms
empty = room('an empty room',
            'The stone floors and walls are cold and damp.',
            './images/empty.png')
temple = room('a small temple',
            'There are three rows of benches facing a small statue.',
            './images/temple.png')
torture = room('a torture chamber',
            'There is a rack and an iron maiden against the wall\nand some chains and thumbscrews on the floor.',
            './images/torture.png')
bedroom = room('a bedroom',
            'There is a large bed with black, silk sheets on it.',
            './images/bedroom.png')

# Setup rooms
empty.add_adjacent_room('east', bedroom)
empty.add_adjacent_room('north', temple)

temple.add_adjacent_room('east', torture)
temple.add_adjacent_room('south', empty)

torture.add_adjacent_room('west', temple)
torture.add_adjacent_room('south', bedroom)

bedroom.add_adjacent_room('north', torture)
bedroom.add_adjacent_room('west', empty)

# Setup items
berries = item('berries', './images/berries.png')
empty.add_item(berries, 100, 100)

# Game state
holding = []
current_room = empty

def draw_current_room():
    screen.blit(current_room.background, (0, 0))
    for item in current_room.items:
        screen.blit(item.icon, (item.x, item.y))

def draw_player():
    screen.blit(player, (x, y))
    for item in holding:
        screen.blit(item.icon, (x + 60, y + 120))

def pick_up_or_drop():
    if len(holding) == 0:
        for item in current_room.items:
            if (item.x >= x) and (item.x <= (x + player_width)):
                if (item.y >= y) and (item.y <= (y + player_height)):
                    current_room.remove_item(berries)
                    holding.append(berries)
    elif len(holding) == 1:
        item = holding[0]
        holding.remove(item)
        current_room.add_item(item, x + 60, y + 120)

# Game loop
while game_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                x_change = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                y_change = 0
            if event.key == pygame.K_SPACE:
                pick_up_or_drop()

    x += x_change
    y += y_change

    # East / Right
    if x > right_edge:
        if "east" in current_room.directions:
            current_room = current_room.directions["east"]
            x = left_edge
        else:
            x = right_edge
    # West / Left
    if x < left_edge:
        if "west" in current_room.directions:
            current_room = current_room.directions["west"]
            x = right_edge
        else:
            x = left_edge
    # South / Bottom
    if y > bottom_edge:
        if "south" in current_room.directions:
            current_room = current_room.directions["south"]
            y = top_edge
        else:
            y = bottom_edge
    # North / Top
    if y < top_edge:
        if "north" in current_room.directions:
            current_room = current_room.directions["north"]
            y = bottom_edge
        else:
            y = top_edge

    draw_current_room()
    draw_player()

    pygame.display.update()
