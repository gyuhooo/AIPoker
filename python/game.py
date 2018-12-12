import pygame
from pygame.locals import *
import sys
import os
import player
import cpu
import distribute as db
import exchange as ex
import animation as an
import time

SCREEN_SIZE = (890, 630)
GREEN = (88, 191, 63)
root = "../images/cards/"
v_root = "../images/voice/"
b_root = "../images/buttons/"
player_cards, cpu_cards, remainder_cards, event, flag =  [], [], [], [], []
GAME_MODE = {'START' : 0, 'DISTR' : 1, 'PLAY' : 2, 'RESULT' : 3}
RESULT = {'NONE' : 0, 'WIN' : 1, 'LOSE' : 2}
game_state, x, y, screen, font, i, button, control, cardback, game_result = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
class Porker(object) :
    
    def __init__(self) :
        pygame.init()
        pygame.font.init
        self.event = pygame.event.get()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Porker')
        self.image_road()
        self.clock = pygame.time.Clock()
        self.game_state = GAME_MODE['START']
        self.game_result = RESULT['NONE']
        self.flag = [False] * 7
        self.button, self.control = False, False
        self.i = -1
        
        while(1) :
            self.clock.tick(100)
            self.screen.fill(GREEN)
            self.x, self.y = pygame.mouse.get_pos()
            self.event = pygame.event.get()
            self.update()
            pygame.display.update()
            self.key_handler()
            pygame.event.clear()
            

    def update(self) : # devide the operetion
        
        if self.game_state == GAME_MODE['PLAY'] :
            for eve in self.event :
                if eve.type == KEYDOWN :
                    if eve.key == K_RIGHT or K_LEFT :
                        pygame.mouse.set_visible(False)
                        self.control = True
                if eve.type == MOUSEMOTION :
                    pygame.mouse.set_visible(True)
                    self.control = False
            self.play()
            if self.flag[5] == True :
                ex.redistr()
                self.cards_reroad()
                self.flag = [False] * 7
            if self.flag[6] == True :
                self.result()
                pygame.display.update()
                #self.voice()
                self.flag = [False] * 7
        elif self.game_state == GAME_MODE['DISTR'] :
            self.cards_road() # cards images road here
            an.animation(self.screen, GREEN, self.clock, self.cardback)
            pygame.time.wait(1000)
            self.game_state = GAME_MODE['PLAY']
            self.clock.tick(100)
        elif self.game_state == GAME_MODE['START'] :
            self.start()
        elif self.game_state == GAME_MODE['RESULT'] :
            self.game_skip()
            time.sleep(3)
            self.game_state = GAME_MODE['START']
        

    def play(self) :
        
        j = 0
        while (j < 5) :
            if self.flag[j] :
                if j != self.i :
                    self.screen.blit(player_cards[j], (265 + j * 60, 390))
            else :
                if j != self.i :
                    self.screen.blit(player_cards[j], (265 + j * 60, 430))
            j += 1
            
        if 0 <= self.i <= 4 :
            self.screen.blit(player_cards[self.i], (265 + self.i * 60, 390))

        if self.i == 5 :
            self.screen.blit(self.button_call, (605, 480))
        else :
            self.screen.blit(self.button_call_on, (605, 480))
        
        if self.i == 6 :
            self.screen.blit(self.button_fold, (725 , 480))
        else :
            self.screen.blit(self.button_fold_on, (725 , 480))

        if self.control :
            self.key_choice()
        else :
            self.mouse_choice()

        self.click(self.i)

        self.print_deck()
        self.print_cpudist()

        self.screen.blit(self.font.render(player.role_comment(), True, (255, 0, 0)), (260, 330))
    
    def result(self) :

        if player.player_role() > cpu.cpu_role() :
            self.game_result == RESULT['WIN']
        else :
            self.game_result == RESULT['LOSE']
        print(cpu.role_comment())
        j = 0
        while (j < 5) :
            self.screen.blit(cpu_cards[j], (265 + j * 60, 90))
            j += 1
        
        self.game_state = GAME_MODE['RESULT']

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
            self.screen.blit(self.title.render('AIPoker', True, (0, 0, 0)), (280, 210))
            self.screen.blit(self.comment.render("Prease click space or press enter.", True, (0, 0, 0)), (260, 340))
        else :
            self.screen.blit(self.title.render('AIPoker', True, (0, 0, 0)), (280, 210))
            self.screen.blit(self.comment.render("Prease click space or press enter.", True, (0, 0, 0)), (260, 340))
            for eve in self.event :
                if eve.type == MOUSEBUTTONDOWN and eve.button == 1 :
                    self.game_state = GAME_MODE['DISTR']
                if eve.type == KEYDOWN :
                    if eve.key == K_RETURN :
                        self.game_state = GAME_MODE['DISTR']

    def click(self, no) :
        for eve in self.event :
            if (eve.type == MOUSEBUTTONDOWN and eve.button == 1) or (eve.type == KEYDOWN and eve.key == K_RETURN) :
                if self.i != -1 :
                    if self.flag[no] :
                        self.flag[no] = False
                    else :
                        self.flag[no] =True
                    if 0 <= no <= 4 :
                        ex.click(no)
        
    def mouse_choice(self) :
        if 390 <= self.y <= 540 :
            if 505 < self.x <= 575 :                            
                self.i = 4
            elif 445 < self.x <= 505 :
                self.i = 3
            elif 385 < self.x <= 445 :
                self.i = 2
            elif 325 < self.x <= 385 :
                self.i = 1
            elif 265 < self.x <= 325 :
                self.i = 0
            else :
                self.i = -1
            if (480 <= self.y <= 520) :
                if 605 < self.x <= 705:
                    self.i = 5
                elif 725 < self.x <= 825 :
                    self.i = 6
        else :
            self.i = -1

    def key_choice(self) :
        for eve in self.event :
            if eve.type == KEYDOWN :
                if eve.key == K_RIGHT :
                    if self.i == -1 :
                        self.i = 0
                    elif self.i != 6 :
                        self.i += 1
                if eve.key == K_LEFT :                    
                    if self.i == -1 :
                        self.i = 4
                    elif self.i != 0 :
                        self.i -= 1

    def cards_road(self) :
        db.distribute()
        global player_cards, cpu_cards, remainder_cards
        player_cards, cpu_cards, remainder_cards = [], [], []
        for no in db.player_num :
            player_cards.append(pygame.image.load("%s%d.png" % (root, no)).convert_alpha())
        for no in db.cpu_num :
            cpu_cards.append(pygame.image.load("%s%d.png" % (root, no)).convert_alpha())
        for no in db.remainder_num :
            remainder_cards.append(pygame.image.load("%s%d.png" % (root, no)).convert_alpha())

    def cards_reroad(self) :
        i = 0
        for no in db.player_num :
            player_cards[i] = (pygame.image.load("%s%d.png" % (root, no)).convert_alpha())
            i += 1

    def image_road(self) :
        self.font = pygame.font.Font("../images/Pacifico.ttf", 40)
        self.title = pygame.font.Font("../images/Pacifico.ttf", 90)        
        self.comment = pygame.font.Font("../images/Pacifico.ttf", 30)
        self.cardback = pygame.image.load("%scardback.png" % root).convert_alpha()
        self.button_call = pygame.image.load("%shit_button_blue.png" % b_root).convert_alpha()
        self.button_call_on = pygame.image.load("%shit_button_blue_fade.png" % b_root).convert_alpha()
        self.button_fold = pygame.image.load("%sstand_button_blue.png" % b_root).convert_alpha()
        self.button_fold_on = pygame.image.load("%sstand_button_blue_fade.png" % b_root).convert_alpha()
        
    def voice(self) :
        pygame.mixer.init(44100, 16, 2, 4096)
        if self.game_result == RESULT['WIN'] :
            pygame.mixer.music.load('%syouwin.mp3' % v_root)
        elif self.game_result == RESULT['LOSE'] :
            pygame.mixer.music.load('%syoulose.mp3' % v_root)
        pygame.mixer.music.play(1)
        self.flag[6] = False
        self.game_state = GAME_MODE['RESULT']
        time.sleep(4)
        
    def game_skip(self) :
        for eve in self.event :
            if (eve.type == MOUSEBUTTONDOWN and eve.button == 1) or (eve.type == KEYDOWN and eve.key == K_RETURN) :
                if self.game_state == GAME_MODE['DISTR'] :
                    self.game_state = GAME_MODE['PLAY']
                elif self.game_state == GAME_MODE['RESULT'] :
                    self.game_state = GAME_MODE['START']

    def print_deck(self) :
        self.screen.blit(self.cardback, (700, 100))
        self.screen.blit(self.cardback, (700, 90))
        self.screen.blit(self.cardback, (700, 80))
        self.screen.blit(self.cardback, (700, 70))

    def print_cpudist(self) :
        self.screen.blit(self.cardback, (265, 90))
        self.screen.blit(self.cardback, (325, 90))
        self.screen.blit(self.cardback, (385, 90))
        self.screen.blit(self.cardback, (445, 90))
        self.screen.blit(self.cardback, (505, 90))

if __name__ == "__main__" :
    MY_GAME = Porker()