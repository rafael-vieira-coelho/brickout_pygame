"""
 Sample Breakout Game
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
# --- Import libraries used for this program
 
from settings import Settings
from game_functions import *

# Call this function so the Pygame library can initialize itself
pygame.init()
# Create Settings
s = Settings()
# Set the title of the window
pygame.display.set_caption(s.title)
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
# Clock to limit speed
clock = pygame.time.Clock()
# Is the game over?
game_over = False
# Draw the game
player, ball, balls, blocks, allsprites = desenho_inicial(s)
# Main program loop
while True:
     # Limit to 30 fps
    clock.tick(30)
    # Clear the screen
    s.screen.fill(s.black)
    testa_eventos()
    verifica_fim_jogo(game_over, player, ball, s)
    verfica_colisoes(player, balls, ball, blocks, s)
    atualiza_tela(allsprites, s)
 
