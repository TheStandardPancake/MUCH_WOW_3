#Thought that the third installment of MUCH WOW would be in 3D, lol no that's too hard. This time it's street fighter style. ~Boyd kirkman

import pygame
from pygame.locals import *

width = 1280
height = 720
pygame.init()

def required():
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~The Main Loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    #setting the background
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Doge Brawl")


    #Testing doge sprite
    doge = Doge()
    doge.rect.x = 500
    doge.rect.y = 300

    while True:
        window.blit(pygame.image.load('backdrop.png'),(0,0))
        doge.update()
        window.blit(doge.image,doge.rect)
        required()
        pygame.display.update()

class Doge(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        global skin
        skin = "StandingDoge.png"
        self.image = pygame.image.load(skin).convert_alpha()
        self.rect = self.image.get_rect()

        global tick
        tick = 0
        global tock
        tock = 0

    def update(self):
        global skin
        global tick
        global tock
        tick += 1
        if tick == 20:
            tock +=1
            tick = 0
        if tock % 2 == 0:
            skin = "StandingDoge1.png"
        if tock % 2 != 0:
            skin = "StandingDoge.png"
        self.image = pygame.image.load(skin).convert_alpha()




if __name__ == "__main__":
    main()
