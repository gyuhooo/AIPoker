import pygame
from pygame.locals import *
import sys
import time
v_root = "../images/voice/"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("%syouwin.mp3" % v_root)
#voice_win = pygame.mixer.Sound("%syouwin.wav" % v_root)
screen = pygame.display.set_mode((860,780))

while(1) :
    #voice_lose.play()
    #voice_win.play()
    
    pygame.mixer.music.play(1)
    time.sleep(3)
    pygame.display.update()

    for eve in pygame.event.get() :
        if eve.type == QUIT :
            sys.exit()
        if eve.type == KEYDOWN :
            if eve.key == K_ESCAPE :
                sys.exit()