#Thought that the third installment of MUCH WOW would be in 3D, lol no that's too hard. This time it's super smash style. ~Boyd kirkman

import pygame
from pygame.locals import *
import random

width = 1280
height = 720
pygame.init()

def required():
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        quit()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Title Screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def title():
    #setting the background
    global window
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Super MUCH WOW: Ultimate")

    #music
    pygame.mixer.music.load("Battle.mp3")
    pygame.mixer.music.play()

    while True:
        window.blit(pygame.image.load('Doge Brawl.png'),(0,0))
        required()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            main()
        pygame.display.update()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~The Main Loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    #music
    pygame.mixer.music.load("Title.mp3")
    pygame.mixer.music.play()

    #powermode
    global powermode
    powermode = False


    #spawning the sprites
    global doge
    doge = Doge()
    doge.rect.x = 500
    doge.rect.y = 410

    global elmo
    elmo = Elmo()
    elmo.rect.x = 700
    elmo.rect.y = 410

    global bottle
    bottle = powerbottle()
    bottle.rect = (random.randrange(0,1265),random.randrange(60,250))

    while True:
        window.blit(pygame.image.load('backdrop.png'),(0,0))
        doge.update()
        window.blit(doge.image,doge.rect)
        elmo.update()
        window.blit(elmo.image,elmo.rect)
        bottle.update()
        if pygame.sprite.collide_mask(bottle, elmo) or pygame.sprite.collide_mask(bottle, doge):
            bottle.rect = (random.randrange(0,1265),random.randrange(60,250))
        required()
        pygame.display.update()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Making the Doge fighter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Doge(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Setting up it's image and position
        global skin
        skin = "StandingDoge.png"
        global skinR
        global skinR1
        skinR = "StandingDoge.png"
        skinR1 = "StandingDoge1.png"
        global skinL
        global skinL1
        skinL = "LStandingDoge.png"
        skinL1 = "LStandingDoge1.png"
        global Anim1
        global Anim2
        Anim1 = "StandingDoge.png"
        Anim2 = "StandingDoge1.png"

        #Physics
        global gravity
        gravity = 1
        global pressed_once
        pressed_once = False

        self.image = pygame.image.load(skin).convert_alpha()
        self.rect = self.image.get_rect()

        #setting up the timing for animation
        global tick
        tick = 0
        global tock
        tock = 0

        #making it turn to face different directions
        global Orient
        Orient = 0

    def update(self):
        #Orientation during the animation
        global Orient
        global skinL
        global skinL1
        global skinR
        global skinR1
        global Anim1
        global Anim2

        #changing the skin to make it look like it's tread moves
        global skin
        global tick
        global tock
        tick += 1
        if tick == 10:
            tock +=1
            tick = 0
        if tock % 2 == 0:
            skin = Anim1
        if tock % 2 != 0:
            skin = Anim2
        self.image = pygame.image.load(skin).convert_alpha()

        #moving
        global gravity
        global pressed_once
        if self.rect.y <= 230 and pygame.key.get_pressed()[pygame.K_f]:
            gravity = -1
        elif self.rect.y <= 50:
            gravity = -1
        if self.rect.y >= 410:
            gravity = 1
        if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_f] and self.rect.x < 1241:
            self.rect.x += 5
            Orient = 0
        elif pygame.key.get_pressed()[pygame.K_d] and self.rect.x < 1241:
            self.rect.x += 10
            Orient = 0
        if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_f] and self.rect.x > 0:
            self.rect.x -= 5
            Orient = 1
        elif pygame.key.get_pressed()[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 10
            Orient = 1
        if pygame.key.get_pressed()[pygame.K_w] and self.rect.y <= 410 and self.rect.y >= 50 and pressed_once == False:
            self.rect.y -= 20*gravity
        elif self.rect.y < 410:
            pressed_once = True
            self.rect.y += 20
        if self.rect.y >= 410:
            self.rect.y = 410
            pressed_once = False


        #checking Orientation
        if Orient == 1 and pygame.key.get_pressed()[pygame.K_f]:
            Anim1 = "LattackDoge.png"
            Anim2 = "LattackDoge.png"
        elif Orient == 1:
            Anim1 = skinL
            Anim2 = skinL1
        if Orient == 0 and pygame.key.get_pressed()[pygame.K_f]:
            Anim1 = "attackDoge.png"
            Anim2 = "attackDoge.png"
        elif Orient == 0:
            Anim1 = skinR
            Anim2 = skinR1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Making the Elmo fighter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Elmo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Setting up it's image and position
        global Eskin
        Eskin = "StandingElmo.png"
        global EskinR
        global EskinR1
        EskinR = "RStandingElmo.png"
        EskinR1 = "RStandingElmo1.png"
        global EskinL
        global EskinL1
        EskinL = "StandingElmo.png"
        EskinL1 = "StandingElmo1.png"
        global EAnim1
        global EAnim2
        EAnim1 = "StandingElmo.png"
        EAnim2 = "StandingElmo1.png"

        #Physics
        global Egravity
        Egravity = 1
        global Epressed_once
        Epressed_once = False

        self.image = pygame.image.load(Eskin).convert_alpha()
        self.rect = self.image.get_rect()

        #setting up the timing for animation
        global Etick
        Etick = 0
        global Etock
        Etock = 0

        #making it turn to face different directions
        global EOrient
        EOrient = 0

    def update(self):
        #Orientation during the animation
        global EOrient
        global EskinL
        global EskinL1
        global EskinR
        global EskinR1
        global EAnim1
        global EAnim2

        #changing the skin to make it look like it's tread moves
        global Eskin
        global Etick
        global Etock
        Etick += 1
        if Etick == 10:
            Etock +=1
            Etick = 0
        if Etock % 2 == 0:
            Eskin = EAnim1
        if Etock % 2 != 0:
            Eskin = EAnim2
        self.image = pygame.image.load(Eskin).convert_alpha()

        #moving
        global Egravity
        global Epressed_once
        if self.rect.y <= 230 and pygame.key.get_pressed()[pygame.K_RCTRL]:
            Egravity = -1
        elif self.rect.y <= 50:
            Egravity = -1
        if self.rect.y >= 410:
            Egravity = 1
        if pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_RCTRL] and self.rect.x < 1241:
            self.rect.x += 5
            EOrient = 0
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.x < 1241:
            self.rect.x += 10
            EOrient = 0
        if pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_RCTRL] and self.rect.x > 0:
            self.rect.x -= 5
            EOrient = 1
        elif pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 10
            EOrient = 1
        if pygame.key.get_pressed()[pygame.K_UP] and self.rect.y <= 410 and self.rect.y >= 50 and Epressed_once == False:
            self.rect.y -= 20*Egravity
        elif self.rect.y < 410:
            Epressed_once = True
            self.rect.y += 20
        if self.rect.y >= 410:
            self.rect.y = 410
            Epressed_once = False


        #checking Orientation
        if EOrient == 1 and pygame.key.get_pressed()[pygame.K_RCTRL]:
            EAnim1 = "attackElmo.png"
            EAnim2 = "attackElmo.png"
        elif EOrient == 1:
            EAnim1 = EskinL
            EAnim2 = EskinL1
        if EOrient == 0 and pygame.key.get_pressed()[pygame.K_RCTRL]:
            EAnim1 = "RattackElmo.png"
            EAnim2 = "RattackElmo.png"
        elif EOrient == 0:
            EAnim1 = EskinR
            EAnim2 = EskinR1

#~~~~~~~~~~~~~~~~~~Inventing the combat system through powerup~~~~~~~~~~~~~~~~~~

class powerbottle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("powerbottle.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        global window
        window.blit(self.image, self.rect)



if __name__ == "__main__":
    title()
