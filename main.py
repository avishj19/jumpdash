import pygame
import random
import time
from geo import Geo
from obstacle import Obstacle
from button import Button
from bluegeo import Bluegeo
from scarygeo import Scarygeo
from musicbutton import Muiscbutton
from classicalbutton import Classicalbutton
from rapbutton import Rapbutton
from backbutton import Backbutton
from fowardbutton import Fowardbutton

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Nexa', 70)
my_font2 = pygame.font.SysFont('Times new roman', 14)
pygame.display.set_caption("Jump Dash")

# set up variables for the display
size = (1000, 600)
screen = pygame.display.set_mode(size)
game_start_screen = True
chose_music = True
choose_sprite = True
game = True
bl_sprite = False
g_sprite = False
s_sprite = False
sprite_collide = False
sprite_selected = None
start_time = time.time()

obstacles = []
bg = pygame.image.load("background.png")
sbg = pygame.image.load("startscreen.png")
g = Geo(10,400)
t = Obstacle(300,400)
b = Button(320,180)
bl = Bluegeo(400,300)
sg = Scarygeo(300,300)
mb = Muiscbutton(600,200)
cb = Classicalbutton(100,300)
rb = Rapbutton(600,330)
bb = Backbutton(10,10)
fb = Fowardbutton(800,8)

x = 300
y = 400
for i in range(5):
    t = Obstacle(x, y)
    obstacles.append(t)
    x = x + 300
    #y += 100

print(obstacles)
backgound_music = pygame.mixer_music.load("rmusic.mp3")
pygame.mixer.music.play(-1)
# Render the text later
start_game_message = my_font.render("Jump Dash",True,(3, 236, 252))
choose_sprite_text = my_font.render("Choose your sprite to play with",True,(3, 236, 252))
music_text = my_font.render("choose your music", True, (3, 236, 252))
loose_message = my_font2.render("YOU LOST", True,(4,26,234))
# -------- Main Program Loop -----------

while game_start_screen:
    screen.blit(sbg,(0,0))
    screen.blit(start_game_message,(320,30))
    screen.blit(b.image,b.rect)
    screen.blit(mb.image,mb.rect)
    pygame.display.update()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_start_screen = False
            chose_music = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if b.rect.collidepoint(event.pos):
             game_start_screen = False
             chose_music = False
            if mb.rect.collidepoint(event.pos):
                game_start_screen = False
                choose_sprite = False
                game = False

while chose_music:
    screen.blit(sbg,(0,0))
    screen.blit(music_text,(250,30))
    screen.blit(cb.image,cb.rect)
    screen.blit(rb.image,rb.rect)
    screen.blit(bb.image,bb.rect)
    screen.blit(fb.image,fb.rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start_screen = False
            chose_music = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if cb.rect.collidepoint(event.pos):
                backgound_music = pygame.mixer_music.load("music.mp3")
                pygame.mixer.music.play(-1)
            if rb.rect.collidepoint(event.pos):
                backgound_music = pygame.mixer_music.load("rmusic.mp3")
                pygame.mixer.music.play(-1)
            if bb.rect.collidepoint(event.pos):
                game_start_screen = True
                chose_music = False
                game_start_screen = True
            if fb.rect.collidepoint(event.pos):
                chose_music = False
                choose_sprite = True


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
            chose_music = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if bl.rect.collidepoint(event.pos):
                #bl_sprite = True
                sprite_selected = bl
                sprite_selected.x_position = 10
                sprite_selected.y_position = 400
                choose_sprite = False
            if g.rect.collidepoint(event.pos):
                #g_sprite = True
                sprite_selected = g
                choose_sprite = False
            if sg.rect.collidepoint(event.pos):
                    #s_sprite = True
                    sprite_selected = sg
                    sprite_selected.x_position = 10
                    sprite_selected.y_position = 400
                    choose_sprite = False

clock = pygame.time.Clock()

while game:
    current_time = time.time()
    run_time = current_time - start_time
    display_time = my_font2.render("Timer: " + str(round(run_time, 2)), True, (0, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if sprite_collide:
                    sprite_collide = False
                    sprite_selected.x_position = 0
                    sprite_selected.y_position = 400
                    start_time = time.time()

                else:
                    sprite_selected.jump()

    sprite_selected.move_geo()
    sprite_selected.x_position = sprite_selected.x_position + 10
    if sprite_selected.x_position >= 1000:
        sprite_selected.x_position = 0


    screen.blit(bg, (0, 0))  # Background

    for t in obstacles:
        if sprite_selected.rect.colliderect(t.rect):
            sprite_collide = True
        if not sprite_collide:
            screen.blit(t.image, t.rect)
            screen.blit(display_time, (10, 10))

    if sprite_collide:
        screen.blit(loose_message, (230, 10))
    else:
        screen.blit(sprite_selected.image, (sprite_selected.x_position, sprite_selected.y_position))

    pygame.display.update()
    clock.tick(60)