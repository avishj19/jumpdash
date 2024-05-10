import pygame
import random
from geo import Geo
from obstacle import Obstacle
from button import Button
from bluegeo import Bluegeo

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Jump Dash")

# set up variables for the display
size = (1000, 600)
screen = pygame.display.set_mode(size)
game_start_screen = True
choose_sprite = True
game = True

obstacles = []
bg = pygame.image.load("background.png")
g = Geo(0,400)
t = Obstacle(300,400)
b = Button(290,220)
bl = Bluegeo(0,400)

x = 300
y = 400
for i in range(5):
    t = Obstacle(x, y)
    obstacles.append(t)
    x = x + 300
    #y += 100

print(obstacles)
#backgound_music = pygame.mixer_music.load("music.mp3")
#pygame.mixer.music.play(-1)
# Render the text later
start_game_message = my_font.render("testing",True,(0,0,255))
# -------- Main Program Loop -----------

while game_start_screen:
    screen.blit(bg,(0,0))
    screen.blit(start_game_message,(100,100))
    screen.blit(b.image,b.rect)
    pygame.display.update()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_start_screen = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if b.rect.collidepoint(event.pos):
             game_start_screen = False
             #choose_sprite = True

while choose_sprite:
    screen.blit(bg, (0, 0))
    screen.blit(g.image,(200,300))
    screen.blit(bl.image,(300,300))
    pygame.display.update()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_start_screen = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
               choose_sprite = False
              # game = True

while game:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game = False
    keys = pygame.key.get_pressed() # Balloon movement
    if keys[pygame.K_SPACE]:
        g.move_geo("up")

    screen.blit(bg, (0, 0))  # Background
    screen.blit(g.image, g.rect)
    for t in obstacles:
        screen.blit(t.image,t.rect)
    pygame.display.update()