import pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, initLocation, screenWidth,screenHeight,heightOffset):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.transform.scale(pygame.image.load(image_file), (screenWidth, screenHeight))
        self.x, self.y = initLocation
        self.resetLocation = (screenWidth,0+heightOffset)
        self.resetTrigger = -screenWidth
    def scrollLeft(self, scrollspeed):
        self.x -= scrollspeed 
        if self.x <= self.resetTrigger:
            self.reset()
    def reset(self):
        self.x, self.y = self.resetLocation

