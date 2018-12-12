import pygame
from pygame.locals import *
import sys

def animation(screen, color, clock, cardback) :
    cards = 0
    flag = [False] * 10 
    root = "../images/cards/"
    i = 0

    while(cards < 10) :
        clock.tick(1)
        if cards < 5 :                
            x = (700 - (265 + cards * 60)) / 200.0
            x1 = x
            y = (430 - 70) / 200.0
            y1 = y
        else :
            x = (700 - (265 + (cards - 5) * 60)) / 200.0
            x1 = x
            y = (90 - 70) / 200.0
            y1 = y

        i = 0
        while (i < 200) :

            screen.blit(cardback, (700, 100))
            screen.blit(cardback, (700, 90))
            screen.blit(cardback, (700, 80))
            screen.blit(cardback, (700, 70))

            screen.blit(pygame.image.load("%scardback.png" % root).convert_alpha(), (700 - x, 70 + y))
            pygame.display.update()

            i += 1
            
            if i == 200 :
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