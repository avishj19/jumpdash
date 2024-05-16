import pygame


class Geo:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("geo.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3
        self.x_positon, self.y_postion = 10, 400
        self.Y_gravity = 1
        self.jump_height = 20
        self.y_velocity = self.jump_height

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_geo(self,):
       self.y_postion -= self.y_velocity
       self.y_velocity -= self.Y_gravity
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


