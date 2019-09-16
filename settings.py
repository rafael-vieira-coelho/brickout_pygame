import pygame

class Settings():

    def __init__(self):
        self.title = 'Breakout'
        # Define some colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        # Size of break-out blocks
        self.block_width = 23
        self.block_height = 15
        # Create an 800x600 sized screen
        self.screen = pygame.display.set_mode([800, 600])
        # This is a font we use to draw text on the screen (size 36)
        self.font = pygame.font.Font(None, 36)
        # Create a surface we can draw on
        self.background = pygame.Surface(self.screen.get_size())
        # The top of the block (y position)
        self.top = 80
        # Number of blocks to create
        self.blockcount = 32
