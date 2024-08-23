import sys # we'll use this module to exit the game when the player quits

import pygame

from setting import settings

from ship import Ship

def run_game():
    pygame.init() # this line initializes the bg settings that pygame needs to work properly at
    ai_settings = settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width , ai_settings.screen_height )) # to create a display window called screen , (1277,651) is used to
    # specify dimension of game window it means 1278 X 658 pixels.
    # A surface in Pygame is a part of the screen where you display a game element. Each element in the game, like 
    # the aliens or the ship, is a surface.
    # note - these parameters are predefined first parameter is width and second is height.

    pygame.display.set_caption("Alien Invasion")

    # Making a ship

    ship = Ship(screen)

    # note - In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you 
    # go down and to the right. On a 1200 by 800 screen, the origin is at the top-left corner, and the bottom-right 
    # corner has the coordinates (1200, 800).

# Setting bg colour(Pygame creates a black bg by default)
    # bg_colour = (0, 0, 139)
    # Redraw the screen during each pass through the loop.

    screen.fill(ai_settings.bg_colour)

       # for keyboard and mouse events.
    while True:
        # An event is an action that the user performs while playing the game, such as pressing a key or moving the 
        # mouse.
        ship.blitme() # it brings ship on screen
        for event in pygame.event.get(): # any event will active for loop 
            if event.type == pygame.QUIT : 
                sys.exit()
        pygame.display.flip() # it shows changes on screen due to an event

run_game()
