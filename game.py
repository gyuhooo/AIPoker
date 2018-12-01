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
        i = 0
        for card in cards :
            screen.blit(card, (200 + i, 300))
            i += 40

        screen.blit(font.render(player.comment, True, (255, 0, 0)), (160, 240))
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pygame.quite()
                sys.exit()
            
        pygame.display.update()

class Card_choice(pygame.sprite.Sprite) :
    animecycle = 12
    frame = 0
    def __init__(self, card, x, y) :
        pygame.sprite.Sprite.__init__(self, self.containers)
        

            
if __name__ == "__main__" :
    MY_GAME = Porker()

