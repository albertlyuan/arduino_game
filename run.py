import pyfirmata
import time
import pygame
from objects import *

def game(arduino):
    if arduino:
        board = pyfirmata.Arduino('COM3')
        it = pyfirmata.util.Iterator(board)
        it.start()
        digital_input = board.get_pin('d:10:i')
        led = board.get_pin('d:13:o')  
        rotary_dt = board.get_pin('d:5:i')
        rotary_clk = board.get_pin('d:4:i')
        no_clk = rotary_clk.read()

    #init game
    pygame.init()
    width = 800
    height = 600
    bgOffset = 100
    groundlevel = height/2 + bgOffset
    SCROLL_SPEED = 3

    #objects
    bg1 = Background("background.png",[0,bgOffset],width,height,bgOffset)
    bg2 = Background("background.png",[width,bgOffset],width,height,bgOffset)
    dino = Dino("dino.gif", groundlevel)
    cacti = Cacti("cactus.png", groundlevel,width)


    screen = pygame.display.set_mode((width,height))
    count = 0

    while True:
        screen.fill([255, 255, 255])
        screen.blit(bg1.image, (bg1.x, bg1.y))
        screen.blit(bg2.image, (bg2.x, bg2.y))
        screen.blit(dino.image, (dino.x, dino.y))
        screen.blit(cacti.image, (cacti.x, cacti.y))
        if arduino:
            sw = digital_input.read()

        #check exit out
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if not arduino:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dino.jump()

        #check endgame
        if dino.rect.colliderect(cacti.rect):
            pass
            """
            print("dead")
            for i in range(6):
                led.write(1)
                time.sleep(0.1)
                led.write(0)
                time.sleep(0.1)
            exit(0)
            """
        
        #check arduino input
        if arduino:
            clk = rotary_clk.read()
           
            if clk != no_clk:
                dt = rotary_dt.read()       
                print("clk: ",clk)
                print("prevclk: ",no_clk)
                print("dt: ",dt)


                if dt == no_clk: #clock if dt false
                    print("CLOCK")
                    SCROLL_SPEED += 1
                else:#counter clock if dt true
                    print("COUNTERCLOCK")
                    if SCROLL_SPEED > 0:
                        SCROLL_SPEED -= 1
                print(f"SCROLL SPEED: {SCROLL_SPEED}")
                no_clk = clk

            if sw is True:
                led.write(1)
                dino.jump()
            else:
                led.write(0)
        
                
        bg1.scrollLeft(SCROLL_SPEED)
        bg2.scrollLeft(SCROLL_SPEED)
        dino.update()
        cacti.update(SCROLL_SPEED)

        pygame.display.update()

if __name__ == "__main__":
    game(arduino=True)
