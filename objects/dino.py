import pygame
from pygame import Rect

DEFAULT_IMAGE_SIZE = 50
JUMP_HEIGHT = 8
GRAVITY_CONSTANT = 0.1

class Dino(pygame.sprite.Sprite):
    def __init__(self, image_file, groundlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image_file), (DEFAULT_IMAGE_SIZE,DEFAULT_IMAGE_SIZE))
        self.ground = groundlevel - DEFAULT_IMAGE_SIZE
        self.y = self.ground
        self.dy = 0
        self.x = 100
        self.dx = 0
        self.jumping = False
        self.rect = Rect(self.x,self.y,DEFAULT_IMAGE_SIZE,DEFAULT_IMAGE_SIZE)

        
    def jump(self):
        if not self.jumping:
            self.dy = -JUMP_HEIGHT
            self.jumping = True

    def update(self):
        self.gravity()
        self.y += self.dy
        self.x += self.dx
        self.rect.left = self.x
        self.rect.top = self.y

    def gravity(self):
        if self.jumping:
            self.dy = self.dy + GRAVITY_CONSTANT
            self.checkGround()

    def checkGround(self):
        if self.y + self.dy > self.ground:
            self.dy = 0
            self.y = self.ground
            self.jumping = False
            