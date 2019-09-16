import pygame
from player import Player
from ball import Ball
from block import Block
import sys

def desenho_inicial(s):
    # Create sprite lists
    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    # Create the player paddle object
    player = Player(s)
    allsprites.add(player)
    # Create the ball
    ball = Ball(s)
    allsprites.add(ball)
    balls.add(ball)
    # --- Create blocks
    # Five rows of blocks
    for row in range(5):
        # 32 columns of blocks
        for column in range(0, s.blockcount):
            # Create a block (color,x,y)
            block = Block(s.blue, column * (s.block_width + 2) + 1, s.top, s)
            blocks.add(block)
            allsprites.add(block)
        # Move the top of the next row down
        s.top += s.block_height + 2

    return player, ball, balls, blocks, allsprites

def testa_eventos():
    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def verifica_fim_jogo(game_over, player, ball, s):
    # Update the ball and player position as long
    # as the game is not over.
    if not game_over:
        # Update the player and ball positions
        player.update()
        game_over = ball.update()
    else:  # If we are done, print game over
        text = s.font.render("Game Over", True, s.white)
        textpos = text.get_rect(centerx=s.background.get_width() / 2)
        textpos.top = 300
        s.screen.blit(text, textpos)

def verfica_colisoes(player, balls, ball, blocks, s):
    # See if the ball hits the player paddle
    if pygame.sprite.spritecollide(player, balls, False):
        # The 'diff' lets you try to bounce the ball left or right
        # depending where on the paddle you hit it
        diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)
        # Set the ball's y position in case
        # we hit the ball on the edge of the paddle
        ball.rect.y = s.screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)
    # Check for collisions between the ball and the blocks
    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
    # If we actually hit a block, bounce the ball
    if len(deadblocks) > 0:
        ball.bounce(0)
        # Game ends if all the blocks are gone
        if len(blocks) == 0:
            game_over = True

def atualiza_tela(allsprites, s):
    # Draw Everything
    allsprites.draw(s.screen)
    # Flip the screen and show what we've drawn
    pygame.display.flip()
