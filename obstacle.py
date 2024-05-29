import pygame


class Obstacle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_position = x
        self.y_position = y
        self.image = pygame.image.load("obstacle.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.6, self.image_size[1] * 0.6)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self):
        self.x_position -= self.speed
        self.rect.topleft = (self.x_position, self.y_position)

    def reset_position(self, new_x):
        self.x_position = new_x
        self.rect.topleft = (self.x_position, self.y_position)

    def check_off_screen(self):
        return self.x_position + self.image.get_width() < 0