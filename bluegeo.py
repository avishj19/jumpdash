import pygame


class Bluegeo:

    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y
        self.image = pygame.image.load("bluegeo.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x_position, self.y_position , self.image_size[0], self.image_size[1])
        self.rect = self.image.get_rect(topleft=(self.x_position, self.y_position))
        self.gravity = 1
        self.jump_height = 25
        self.y_velocity = 0
        self.on_ground = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)


    def move_geo(self):
      if not self.on_ground:
        self.y_position += self.y_velocity
        self.y_velocity += self.gravity
        if self.y_position >= 400:
            self.y_position = 400
            self.y_velocity = 0
            self.on_ground = True

      self.rect.topleft = (self.x_position, self.y_position)


    def jump(self):
       if self.on_ground:
          self.y_velocity = -self.jump_height
          self.on_ground = False


    def draw(self, screen):
       screen.blit(self.image, (self.x_position, self.y_position))

    def check_off_screen(self):
        return self.x_position + self.image_size[0] < 0
