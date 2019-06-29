##########################################################
## ADVENTURE GAME STARTS HERE
##########################################################
import random
from adventure import *

# start by creating the game system
game = Game("Brightworks Adventure")

# define and describe a couple of locations
sidewalk = game.new_location(
  "Sidewalk",
"""There is a large glass door to the west.
The sign says 'Come In!'""")

vestibule = game.new_location(
  "Vestibule",
"""A small area at the bottom of a flight of stairs.
There is a glass door to the east, and door to the
west. To the north there is a dark muddy hole.""")

office = game.new_location(
  "Office",
"""A nicely organized office.
There is a door to the south.""")

tunnel = game.new_location(
  "Tunnel",
"""A dark and moist muddy hole that might lead somewhere...""")

game.new_connection("Glass Door", sidewalk, vestibule, [IN, WEST], [OUT, EAST])
game.new_connection("Office Door", vestibule, office, [IN, WEST], [OUT, EAST])
game.new_connection("Tunnel Opening", vestibule, tunnel, [DOWN, NORTH], [UP, SOUTH])

# Now let's add a thing, a key, by providing a single word name and a longer
# description.  We will create the key at the sidewalk.
key = sidewalk.new_object("key", "a small tarnished key")

# And we can make the key required to open the office
office.make_requirement(key)

# Let's add a special phrase. We can attach this phrase to any object, location or actor,
# and the phrase will trigger only if that object or actor is present or at the given location.
key.add_phrase("rub key", game.say("You rub the key, but fail to shine it."))

player = game.new_player(sidewalk)

game.run()
