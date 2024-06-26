import pygame
import random
import time
from geo import Geo
from obstacle import Obstacle
from Startbutton import Startbutton
from bluegeo import Bluegeo
from scarygeo import Scarygeo
from musicbutton import Muiscbutton
from classicalbutton import Classicalbutton
from rapbutton import Rapbutton
from fowardbutton import Fowardbutton

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Nexa', 70)
my_font2 = pygame.font.SysFont('Arial', 25)
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

obstacles = []
bg = pygame.image.load("background.png")
sbg = pygame.image.load("startscreen.png")
g = Geo(30,400)
t = Obstacle(300,400)
b = Startbutton(320,180)
bl = Bluegeo(480,390)
sg = Scarygeo(860,400)
mb = Muiscbutton(600,200)
cb = Classicalbutton(100,300)
rb = Rapbutton(600,330)
fb = Fowardbutton(800,8)
score = 0

# reads the high score file and records the high score using the variable high_score
f = open("highscore", "r")
data = f.readline().strip()
high_score = int(data) if data else 0
f.close()

x = 200
y = 400
# obstacle locations

def reset_obstacles(score):
    global obstacles
    obstacles = []
    x = 200
    for i in range(4):
        t = Obstacle(x, y)
        obstacles.append(t)
        if score < 4:
            x += random.randint(220, 230)
        elif score >= 4 and score < 7:
            x += random.randint(200,230)
        elif score >= 7:
            x += random.randint(200,220)
# Distance between obstacles and regenerates the distance
# everytime the player finishes the obstacles

reset_obstacles(score)

# Render the text later
start_game_message = my_font.render("Jump Dash",True,(3, 236, 252))
choose_sprite_text = my_font.render("Choose your sprite to play with",True,(3, 236, 252))
music_text = my_font.render("choose your music", True, (3, 236, 252))
score_message = my_font2.render("Score: " + str(score), True, ((0, 255, 0)))
high_score_message = my_font2.render("Last High score: " + str(high_score),True,(52, 229, 235))
newrecord_message = my_font2.render("You hit a new Highscore which was: " + str(score),True,(135, 206, 235))
loose_message = my_font.render("YOU LOST", True,(135, 206, 235))
geo_message = my_font2.render("Geo Sprite", True, (255, 253, 208))
bluegeo_message = my_font2.render("Blue Geo Sprite", True, (255, 253, 208))
scarygeo_message = my_font2.render("Scary Geo Sprite", True, (255, 253, 208))

# -------- Main Program Loop -----------

while game_start_screen:
    screen.blit(sbg,(0,0))
    screen.blit(start_game_message,(320,30))
    screen.blit(b.image,b.rect)
    screen.blit(mb.image,mb.rect)
    pygame.display.update()
# User start screen to start the game or if they want to choose play music

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
        # checks the button that they pressed

while chose_music:
    screen.blit(sbg,(0,0))
    screen.blit(music_text,(250,30))
    screen.blit(cb.image,cb.rect)
    screen.blit(rb.image,rb.rect)
    screen.blit(fb.image,fb.rect)
    pygame.display.update()
    # if the user presses on music button
    # it loads the music choices

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start_screen = False
            chose_music = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if cb.rect.collidepoint(event.pos):
                background_music = pygame.mixer_music.load("music.mp3")
                pygame.mixer.music.play(-1)
            if rb.rect.collidepoint(event.pos):
                background_music = pygame.mixer_music.load("rmusic.mp3")
                pygame.mixer.music.play(-1)
            if fb.rect.collidepoint(event.pos): # click this button once they choose the music
                chose_music = False
                choose_sprite = True
        # Based on the button they press, the music will play


while choose_sprite:
    screen.blit(bg, (0, 0))
    screen.blit(choose_sprite_text,(130,50))
    screen.blit(g.image,g.rect)
    screen.blit(bl.image,bl.rect)
    screen.blit(sg.image,sg.rect)
    screen.blit(geo_message,(10, 200))
    screen.blit(bluegeo_message, (445,200))
    screen.blit(scarygeo_message,(790,200))
    pygame.display.update()
    # options for the sprite they want to choose


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_start_screen = False
            chose_music = False
            choose_sprite = False
            game = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if bl.rect.collidepoint(event.pos):
                sprite_selected = bl
                sprite_selected.x_position = 10
                sprite_selected.y_position = 400
                choose_sprite = False
            if g.rect.collidepoint(event.pos):
                sprite_selected = g
                choose_sprite = False
            if sg.rect.collidepoint(event.pos):
                    sprite_selected = sg
                    sprite_selected.x_position = 10
                    sprite_selected.y_position = 400
                    choose_sprite = False
# based on what sprite they click, it sets up the starting position
# Does this by having a variable that allows for the access of that class

clock = pygame.time.Clock() #Frame rate

start_time = time.time()
while game:
    if not sprite_collide:
        current_time = time.time()
    run_time = current_time - start_time
    display_time = my_font2.render("Timer: " + str(round(run_time, 2)), True, (0, 255, 0))
    # Displays a timer for how long the user survived for

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if sprite_collide:
                    sprite_collide = False
                    sprite_selected.x_position = 0
                    sprite_selected.y_position = 400
                    score = 0
                    score_message = my_font2.render("Score: " + str(score), True, ((0, 255, 0)))

                    f = open("highscore", "r")
                    data = f.readline().strip()
                    high_score = int(data) if data else 0
                    f.close()
                    high_score_message = my_font2.render("Last High score: " + str(high_score), True, (52, 229, 235))
                    start_time = time.time()
                else:
                    sprite_selected.jump()

    sprite_selected.move_geo()
    sprite_selected.x_position = sprite_selected.x_position + 5  # moves the sprite
    if sprite_selected.x_position >= 1000 and not sprite_collide:
        score = score + 1
        score_message = my_font2.render("Score: " + str(score), True, ((0, 255, 0)))
        sprite_selected.x_position = 0
        reset_obstacles(score)
    # rests the sprite to the starting position after it goes through all the obstacles
    # also increases his score by 1


    screen.blit(sbg, (0, 0))  # Background

    for t in obstacles:
        if sprite_selected.rect.colliderect(t.rect):
            sprite_collide = True
        # detects collision
        if not sprite_collide:
            screen.blit(t.image, t.rect)
            screen.blit(display_time, (10, 10))
            screen.blit(score_message,(10,40))
            screen.blit(high_score_message, (10,70))
            screen.blit(sprite_selected.image, (sprite_selected.x_position, sprite_selected.y_position))
        # Blits the game if the user has not lost

    if sprite_collide:
        screen.blit(loose_message, (350, 80))
        display_time_survived = my_font2.render("You survived for: " + str(round(run_time, 2)) + " seconds", True, (14, 237, 107))
        screen.blit(display_time_survived,(290,200))
        if score > high_score:
            f = open("highscore", "w")
            f.write(str(score))
            f.close()
            newrecord_message = my_font2.render("You hit a new Highscore which was: " + str(score), True,(135, 206, 235))
            screen.blit(newrecord_message,(260,300))
        # If the user looses, it will show a loose message and how long he survived for
        # If he has beaten his high score, a message will pop up and will record the high score

    pygame.display.update()
    clock.tick(60)