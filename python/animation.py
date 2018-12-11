import pygame
from pygame.locals import *
import sys

def animation(screen, color, clock) :
    cards = 0
    flag = [False] * 10 
    root = "../images/cards/"
    i = 0

    while(cards < 10) :
        clock.tick(1)
        if cards < 5 :                
            x = (700 - (265 + cards * 60)) / 100
            x1 = x
            y = (430 - 70) / 100
            y1 = y
        else :
            x = (700 - (265 + (cards - 5) * 60)) / 100
            x1 = x
            y = (90 - 70) / 100
            y1 = y

        print("x : %d, y : %d" % (x, y))

        i = 0
        while (i < 100) :

            screen.blit(pygame.image.load("%scardback.png" % (root)).convert_alpha(), (700, 100))
            screen.blit(pygame.image.load("%scardback.png" % (root)).convert_alpha(), (700, 90))
            screen.blit(pygame.image.load("%scardback.png" % (root)).convert_alpha(), (700, 80))
            screen.blit(pygame.image.load("%scardback.png" % (root)).convert_alpha(), (700, 70))

            screen.blit(pygame.image.load("%scardback.png" % root).convert_alpha(), (700 - x, 70 + y))
            pygame.display.update()

            i += 1
            
            if i == 100 :
                flag[cards] = True
                cards += 1
            else :
                pygame.draw.rect(screen, color, Rect(700 - x, 70 + y, 775 - x, 180 + y))
            
            x += x1
            y += y1

        for eve in pygame.event.get() :
            if eve.type == QUIT :
                sys.exit()
            if eve.type == KEYDOWN :
                if eve.key == K_ESCAPE :
                    sys.exit()