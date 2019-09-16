"""
 Sample Breakout Game
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
# --- Import libraries used for this program
 
import math
import pygame
 
 
 
class Block(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by the ball
    It derives from the "Sprite" class in Pygame """
 
    def __init__(self, color, x, y, s):
        """ Constructor. Pass in the color of the block,
            and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create the image of the block of appropriate size
        # The width and height are sent as a list for the first parameter.
        self.image = pygame.Surface([s.block_width, s.block_height])
 
        # Fill the image with the appropriate color
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
 
        # Move the top left of the rectangle to x,y.
        # This is where our block will appear..
        self.rect.x = x
        self.rect.y = y
 
 
