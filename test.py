import pyfirmata
import time
import pygame

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
screen = pygame.display.set_mode((width,height))
screen.fill((0,0,0))
pygame.display.update()

count = 0
while True:
    sw = digital_input.read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    if sw is True:
        led.write(1)
        count+=1
        print(count)
    else:
        led.write(0)
    time.sleep(0.1)