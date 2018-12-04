import pygame
from pygame.locals import *
import sys
import os
import player
import distribute as db

SCREEN_SIZE = (640, 480)
GREEN = (88, 191, 63)
root = "../images/cards/"
cards = []
flag = [False, False, False, False, False]
GAME_MODE = {'START' : 0, 'GAME' : 1}

class Porker(object) :

    def __init__(self) :
        pygame.init()
        pygame.font.init
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Porker')
        font = pygame.font.Font("../images/Pacifico.ttf", 40)
        clock = pygame.time.Clock()
        self.game_state = GAME_MODE['START']
        for no in db.num :
            cards.append(pygame.image.load("%s%d.png" % (root, no)).convert_alpha())
            
        while True :
            clock.tick(10)
            x, y = pygame.mouse.get_pos()
            self.draw(screen)
            self.update(screen, font, x, y)
            pygame.display.update()
            self.key_handler()

        #for debug
        #print(x, y)
        
    def draw(self, screen) :
            
        screen.fill(GREEN)
        
    def update(self, screen, font, x, y) :
        if self.game_state == GAME_MODE['GAME'] :
            self.game(screen, font, x, y)
        elif self.game_state == GAME_MODE['START'] :
            self.start()

    def game(self, screen, font, x, y) :
        print("game now")
        for event in pygame.event.get() :
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
        
        screen.blit(font.render(player.comment, True, (255, 0, 0)), (160, 220))

    def start(self) :
        print("start now")
        for event in pygame.event.get() :                
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                self.game_state = GAME_MODE['GAME']       


    def key_handler(self) :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()

"""
class Card_choice(pygame.sprite.Sprite) :
    animecycle = 12
    frame = 0
    def __init__(self, card, x, y) :
        pygame.sprite.Sprite.__init__(self, self.containers)
"""

            
if __name__ == "__main__" :
    MY_GAME = Porker()
    
