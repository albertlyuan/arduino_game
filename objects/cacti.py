import pygame
from pygame import Rect
DEFAULT_IMAGE_SIZE = 80
SCROLL_SPEED = 20

class Cacti(pygame.sprite.Sprite):
    def __init__(self, image_file, groundlevel,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (DEFAULT_IMAGE_SIZE/2,DEFAULT_IMAGE_SIZE))
        self.ground = groundlevel - DEFAULT_IMAGE_SIZE
        self.y = self.ground
        self.resetLocation = width
        self.x = self.resetLocation
        self.resetTrigger = 0-DEFAULT_IMAGE_SIZE
        self.rect = Rect(self.x,self.y,DEFAULT_IMAGE_SIZE/2,DEFAULT_IMAGE_SIZE)

    def update(self, scrollspeed):
        self.x -= scrollspeed
        if self.x <= self.resetTrigger:
            self.reset()
        self.rect.left = self.x
        self.rect.top = self.y

    def reset(self):
        self.x = self.resetLocation