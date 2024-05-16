import pygame
import random
from geo import Geo
from obstacle import Obstacle
from button import Button
from bluegeo import Bluegeo
from scarygeo import Scarygeo

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Nexa', 70)
pygame.display.set_caption("Jump Dash")

# set up variables for the display
size = (1000, 600)
screen = pygame.display.set_mode(size)
game_start_screen = True
choose_sprite = True
game = True
bl_sprite = False
g_sprite = False
s_sprite = False

obstacles = []
bg = pygame.image.load("background.png")
g = Geo(200,200)
t = Obstacle(300,400)
b = Button(290,220)
bl = Bluegeo(300,300)
sg = Scarygeo(250,500)

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
choose_sprite_text = my_font.render("Choose your sprite to play with",True,(3, 236, 252))
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
    screen.blit(choose_sprite_text,(130,50))
    screen.blit(g.image,g.rect)
    screen.blit(bl.image,bl.rect)
    screen.blit(sg.image,sg.rect)
    pygame.display.update()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_start_screen = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if bl.rect.collidepoint(event.pos):
                bl_sprite = True
                choose_sprite = False
            if g.rect.collidepoint(event.pos):
                g_sprite = True
                choose_sprite = False
            if sg.rect.collidepoint(event.pos):
                    s_sprite = True
                    choose_sprite = False



while game:
    x = 10
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game = False
    keys = pygame.key.get_pressed() # Balloon movement
    if keys[pygame.K_SPACE]:
        g.move_geo()


    screen.blit(bg, (0, 0))  # Background
    if g_sprite == True:
        screen.blit(g.image,(10,400))
    if bl_sprite == True:
        screen.blit(bl.image,(10,400))
    if s_sprite == True:
        screen.blit(sg.image,(10,400))
    for t in obstacles:
        screen.blit(t.image,t.rect)
    pygame.display.update()