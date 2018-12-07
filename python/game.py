import pygame
from pygame.locals import *
import sys
import os
import player
import distribute as db
#import exchange as ex

SCREEN_SIZE = (640, 480)
GREEN = (88, 191, 63)
root = "../images/cards/"
cards, event, flag = [], [], []
GAME_MODE = {'START' : 0, 'PLAY' : 1}
game_state, x, y, screen, font, i = 0, 0, 0, 0, 0, 0

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
        self.flag = [False, False, False, False, False, False, False, False]
        self.i = -1
    
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
            for eve in self.event :
                if eve.type == KEYDOWN :
                    if eve.key == K_RIGHT or K_LEFT :
                        pygame.mouse.set_visible(False)
                        self.flag[7] = True
                if eve.type == MOUSEMOTION :
                    pygame.mouse.set_visible(True)
                    self.flag[7] = False
            self.play()               
        elif self.game_state == GAME_MODE['START'] :
            self.start()

    def play(self) :
        
        j = 0
        while (j < 5) :
            if self.flag[j] :
                if j != self.i :
                    self.screen.blit(cards[j], (200 + j * 40, 260))
            else :
                if j != self.i :
                    self.screen.blit(cards[j], (200 + j * 40, 300))
            j += 1
            
        if 0 <= self.i <= 4 :
            self.screen.blit(cards[self.i], (200 + self.i * 40, 260))
        self.click(self.i)
        if self.flag[7] :
            self.key_choice()
        else :
            self.mouse_choice()
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
                if eve.type == KEYDOWN :
                    if eve.key == K_RETURN :
                        self.game_state = GAME_MODE['PLAY']

    def click(self, no) :
        for eve in self.event :
            if (eve.type == MOUSEBUTTONDOWN and eve.button == 1) or (eve.type == KEYDOWN and eve.key == K_RETURN) :
                if self.flag[no] == True :
                    self.flag[no] = False
                else :
                    self.flag[no] =True
        
    def mouse_choice(self) :
        if 260 <= self.y <= 410 :
            if 360 < self.x <= 430 :                            
                self.i = 4
            elif 320 < self.x <= 360 :
                self.i = 3
            elif 280 < self.x <= 320 :
                self.i = 2
            elif 240 < self.x <= 280 :
                self.i = 1
            elif 200 < self.x <= 240 :
                self.i = 0
            else :
                self.i = -1

    def key_choice(self) :
        for eve in self.event :
            if eve.type == KEYDOWN :
                if eve.key == K_RIGHT :
                    if self.i != 4 :
                        self.i += 1
                if eve.key == K_LEFT :
                    if self.i != 0 :
                        self.i -= 1
                        
"""
class Card_choice(pygame.sprite.Sprite) :
    animecycle = 12
    frame = 0
    def __init__(self, card, x, y) :
        pygame.sprite.Sprite.__init__(self, self.containers)
        
"""
             
if __name__ == "__main__" :
    MY_GAME = Porker()
