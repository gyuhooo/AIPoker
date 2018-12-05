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
event = []
flag = []
GAME_MODE = {'START' : 0, 'PLAY' : 1}
game_state, x, y, screen, font = 0, 0, 0, 0, 0

class Porker(object) :
    
    def __init__(self) :
        pygame.init()
        pygame.font.init
        self.event = pygame.event.get()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Porker')
        self.font = pygame.font.Font("../images/Pacifico.ttf", 40)
        self.clock = pygame.time.Clock()
        self.game_state = GAME_MODE['START']
        self.flag = [False, False, False, False, False]
    
        for no in db.player_num :
            cards.append(pygame.image.load("%s%d.png" % (root, no)).convert_alpha())
            
        
        while(1) :
            self.clock.tick(60)
            self.screen.fill(GREEN)
            self.x, self.y = pygame.mouse.get_pos()
            self.event = pygame.event.get()
            self.update()
            pygame.display.update()
            self.key_handler()
            pygame.event.clear()
            

    def update(self) :
        if self.game_state == GAME_MODE['PLAY'] :
            self.play()
        elif self.game_state == GAME_MODE['START'] :
            self.start()

    def play(self) :
        j = 0
        while (j < 5) :
            if self.flag[j] :                
                if 260 <= self.y <= 410 :
                    if j == 4 :
                        if 360 < self.x <= 430 :                            
                            for eve in self.event :
                                if eve.type == MOUSEBUTTONDOWN and eve.button == 1 :
                                    self.flag[j] = False
                            self.screen.blit(cards[j], (200 + j * 40, 260))
                    else :
                        if 200 + j * 40 < self.x <= 240 + j * 40 :
                            for eve in self.event :
                                if eve.type == MOUSEBUTTONDOWN and eve.button == 1 :
                                    self.flag[j] = False
                            self.screen.blit(cards[j], (200 + j * 40, 260))
                self.screen.blit(cards[j], (200 + j * 40, 260))
            else :
                if 300 <= self.y <= 410 :
                    if j == 4 :
                        if 360 < self.x <= 430 :
                            for eve in self.event :
                                if eve.type == MOUSEBUTTONDOWN and eve.button == 1 :
                                    self.flag[j] = True
                            self.screen.blit(cards[j], (200 + j * 40, 260))
                        else :
                            self.screen.blit(cards[j], (200 + j * 40, 300))
                    else :
                        if 200 + j * 40 < self.x <= 240 + j * 40 :
                            for eve in self.event :
                                if eve.type == MOUSEBUTTONDOWN and eve.button == 1 :
                                    self.flag[j] = True
                            self.screen.blit(cards[j], (200 + j * 40, 260))
                        else :
                            self.screen.blit(cards[j], (200 + j * 40, 300))
                else :
                    self.screen.blit(cards[j], (200 + j * 40, 300))
                        
            j += 1

        self.screen.blit(self.font.render(player.comment, True, (255, 0, 0)), (160, 220))
    
    def key_handler(self) :
        if self.event != [] :
            for eve in self.event :
                if eve.type == QUIT :
                    sys.exit()

                if eve.type == KEYDOWN :
                    if eve.key == K_ESCAPE :
                        sys.exit()

    def start(self) :
        if self.event == [] :
            pygame.event.pump()
        else :
            for eve in self.event :
                if eve.type == MOUSEBUTTONDOWN and eve.button == 1 :
                    self.game_state = GAME_MODE['PLAY']
                    print('now')
            
        
"""
class Card_choice(pygame.sprite.Sprite) :
    animecycle = 12
    frame = 0
    def __init__(self, card, x, y) :
        pygame.sprite.Sprite.__init__(self, self.containers)
        
"""
             
if __name__ == "__main__" :
    MY_GAME = Porker()
