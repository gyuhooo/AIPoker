import pygame
from pygame.locals import *
import sys
import os
import player
import distribute as db

SCREEN_SIZE = (640, 480)
GREEN = (88, 191, 63)
root = "./images/cards/"
cards = []
flag = [False, False, False, False, False]

class Porker(object) :
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Porker')
    font = pygame.font.Font("./Pacifico.ttf", 40)
    
    for no in db.num :
        cards.append(pygame.image.load("%s%d.png" % (root, no)).convert_alpha())

    while(1) :
        screen.fill(GREEN)
        x, y = pygame.mouse.get_pos()

        #for debug
        #print(x, y)
        
        i = 0
        #for card in cards :
        j = 0
        while (j < 5) :                
            if flag[j] :                
                if 260 <= y <= 410 :
                    if j == 4 :
                        if 360 < x <= 430 :
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                                flag[j] = False
                    else :
                        if 200 + j * 40 < x <= 240 + j * 40 :
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                                flag[j] = False
                screen.blit(cards[j], (200 + j * 40, 260))
            else :
                if 300 <= y <= 410 :
                    if j == 4 :
                        if 360 < x <= 430 :
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                                flag[j] = True
                            screen.blit(cards[j], (200 + j * 40, 260))
                        else :
                            screen.blit(cards[j], (200 + j * 40, 300))
                    else :
                        if 200 + j * 40 < x <= 240 + j * 40 :
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                                flag[j] = True
                            screen.blit(cards[j], (200 + j * 40, 260))
                        else :
                            screen.blit(cards[j], (200 + j * 40, 300))
                else :
                    screen.blit(cards[j], (200 + j * 40, 300))
                            
            j += 1
            """
            if 300 <= y <= 410 :
                if 200 < x <= 240 :
                    if flag[0] :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[0] = False
                    else :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[0] = True
                        if i == 0 :
                            screen.blit(card, (200 + i, 260))
                elif 240 < x <= 280 :
                    if flag[1] :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[1] = False
                    else :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[1] = True
                        if i == 40 :
                            screen.blit(card, (200 + i, 260))
                elif 280 < x <= 320 :
                    if flag[2] :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[2] = False
                    else :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[2] = True
                        if i == 80 :
                            screen.blit(card, (200 + i, 260))
                elif 320 < x <= 360 :
                    if flag[3] :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[3] = False
                    else :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[3] = True
                        if i == 120 :
                            screen.blit(card, (200 + i, 260))
                elif 360 < x <= 430 :
                    if flag[4] :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[4] = False
                    else :
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            flag[4] = True
                        if i == 160 :
                            screen.blit(card, (200 + i, 260))
                else :
                    screen.blit(card, (200 + i, 300))
            else :
                    screen.blit(card, (200 + i, 300))
                    
            i += 40
        
        j = 0
        while (j < 5) :
            if flag[j] :
                screen.blit(cards[j], (200 + j * 40, 260))
            else :
                screen.blit(cards[j], (200 + j * 40, 300))
            j += 1
        """
        screen.blit(font.render(player.comment, True, (255, 0, 0)), (160, 220))
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()
            """
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                sys.exit()
            """
        pygame.display.update()

class Card_choice(pygame.sprite.Sprite) :
    animecycle = 12
    frame = 0
    def __init__(self, card, x, y) :
        pygame.sprite.Sprite.__init__(self, self.containers)
        

            
if __name__ == "__main__" :
    MY_GAME = Porker()

