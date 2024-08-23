import pygame

class Ship():
    # Initialize the ship and set its starting position.
    def __init__(self, screen) :
        self.screen = screen
    # Load the ship image and get its rect(rectangle).
        self.image = pygame.image.load('Image/flying-cartoon-spaceship_24877-8-_3_-_1_.bmp')
        self.ship_x = 590
        self.ship_y = 520

# note - When working with a rect object, you can use the x- and y-coordinates of the top, bottom, left, and 
# right edges of the rectangle, as well as the center. You can set any of these values to determine the current 
# position of the rect.

    # Start each new ship at the bottom center of the screen.

    def blitme(self):
        # it brings ship on screen
        self.screen.blit(self.image , (self.ship_x , self.ship_y))