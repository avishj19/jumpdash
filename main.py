import pygame
import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Jump Dash")

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
game = True

bg = pygame.image.load("background.png")
# Render the text later

# -------- Main Program Loop -----------
while game:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game = False

    screen.blit(bg, (0, 0))  # Background
    pygame.display.update()