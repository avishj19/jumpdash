import pygame
import random
from geo import Geo

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
g = Geo(0,400)
t = Obstacle(10,400)
# Render the text later

# -------- Main Program Loop -----------
while game:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game = False
    keys = pygame.key.get_pressed() # Balloon movement
    if keys[pygame.K_SPACE]:
        g.move_geo("up")

    screen.blit(bg, (0, 0))  # Background
    screen.blit(g.image, g.rect)
    screen.blit(t.image,t.rect)
    pygame.display.update()