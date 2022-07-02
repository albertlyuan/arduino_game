import pyfirmata
import time
import pygame
from objects import *


#init arduino
board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

#init game
pygame.init()
width = 800
height = 600
bgOffset = 100
groundlevel = height/2 + bgOffset
SCROLL_SPEED = 1.5

#objects
bg1 = Background("background.png",[0,bgOffset],width,height,bgOffset, SCROLL_SPEED)
bg2 = Background("background.png",[width,bgOffset],width,height,bgOffset, SCROLL_SPEED)
dino = Dino("dino.gif", groundlevel)
cacti = Cacti("cactus.png", groundlevel,width,SCROLL_SPEED)


screen = pygame.display.set_mode((width,height))

while True:
    screen.fill([255, 255, 255])
    screen.blit(bg1.image, (bg1.x, bg1.y))
    screen.blit(bg2.image, (bg2.x, bg2.y))
    screen.blit(dino.image, (dino.x, dino.y))
    screen.blit(cacti.image, (cacti.x, cacti.y))
    sw = digital_input.read()

    #check exit out
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    #check endgame
    if dino.rect.colliderect(cacti.rect):
        print("dead")
        time.sleep(1)
        exit(0)
    
    #check arduino input
    if sw is True:
        led.write(1)
        dino.jump()
    else:
        led.write(0)
               
    bg1.scrollLeft()
    bg2.scrollLeft()
    dino.update()
    cacti.update()

    pygame.display.update()

    
