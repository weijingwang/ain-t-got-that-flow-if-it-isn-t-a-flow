#!/usr/bin/python3
import pygame as pg
from displayText import *
import random
# from game import * 
from game import *
pg.mixer.pre_init()
pg.init()
pg.font.init()


#images
scene1 = pg.image.load("assets/images/scene1.png")
scene2 = pg.image.load("assets/images/scene2.png")
scene3 = pg.image.load("assets/images/scene3.png")
scene4 = pg.image.load("assets/images/scene4.png")
blackTexture = pg.image.load("assets/images/back_texture.png")
aki = pg.image.load("assets/images/akiHead.png")
koharu = pg.image.load("assets/images/koharuHead.png")
kaito = pg.image.load("assets/images/kaitoHead.png")
lilHeesoos = pg.image.load("assets/images/lilHeesoosHead.png")
stage = pg.image.load("assets/images/stage1a.png")
#music
# pg.mixer.music.load("assets/sounds/this should be peaceful music yeah?.mp3")
# pg.mixer.music.set_volume(0.5)
# pg.mixer.music.play(-1)
#Sound Effects
sound = pg.mixer.Sound("assets/sounds/player/dk.ogg")


def playVoice(whichVoice):
    pg.mixer.stop()
    whichVoice.play()

def gameIntro(surface):
    done = False
    pictureCount = 0
    backImage = scene1
    sayWhat = None
    scene3Y = -600
    move = False
    person = lilHeesoos
    skip = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pictureCount +=1
                    # print(pictureCount)
                    playVoice(sound)
                elif event.key == pg.K_RETURN:
                    skip = True

            if pictureCount == 0:
                backImage = scene1
                sayWhat = 'Press Space yo and enter to skip '
            elif pictureCount == 1:
                backImage = scene1
                sayWhat = 'and i love burgers and im a rapper yo im the best'
            elif pictureCount == 2:
                backImage = scene1
                sayWhat = 'and im gonna go to a gig now and i love my big macs'
            elif pictureCount == 3:
                backImage = scene2
                sayWhat = 'yoyoyoyo whos burger do you think your fwording messing with shes mine'
            elif pictureCount ==4:
                person = scene3
                sayWhat = 'who da fword u talking 2? you talking to john biggo here yo'
                move = True
            elif pictureCount ==5:
                sayWhat = 'you dont mess with john biggo yo'
            elif pictureCount ==6:
                person = kaito
                backImage = scene4
                sayWhat = 'dudes i ABOSOLUTELY CAN NOT WAIT 4 dis show!!!!! i <3 classical music!'
            elif pictureCount == 7:
                person = koharu
                sayWhat = 'wow omg im so exited!!!!'
            elif pictureCount == 8:
                person = aki
                sayWhat = '...'
            elif pictureCount == 9:
                person = lilHeesoos
                backImage = scene2
                sayWhat = 'you know what? its fworing on >:('
            elif pictureCount ==10:
                person = scene3
                sayWhat = 'com at me bro, show me what u got!!!'
            if skip == True or pictureCount == 11:
                done = True
                instructions(surface)


        surface.blit(backImage,(0,0))
        if move == True:
            scene3Y+=20
            if scene3Y>620:
                move = False

        surface.blit(scene3,(140,scene3Y))#scene 3
        surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
        surface.blit(pg.transform.scale(person, (100, 100)), (0, 500))
        messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
        pg.display.update()

def instructions(surface):
    #music
    pg.mixer.music.stop()
    pg.mixer.music.load("assets/sounds/FreeHipHopBeats-ThePassionHiFi-Foundation-HipHopBeatInstumental.mp3")
    pg.mixer.music.set_volume(1)
    pg.mixer.music.play(-1)
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    done = True
                    startTheGames(surface)

        surface.blit(stage,(0,0))
        surface.blit(pg.transform.scale(blackTexture, (800, 600)), (0, 0))
        messageText("instructions",325,30,40,surface,255,255,255,"Roboto")
        messageText("press 123 123 123 and teach that guy a lesson 4 eating ur burger!",100,90,20,surface,255,255,255,"Roboto")
        messageText("hold corrosponding number for as long as possible while the pointer is still on the point 4 points!",30,130,15,surface,255,255,255,"Roboto")
        messageText("u gotta get that good flow, you know. Press Enter to start",100,160,20,surface,255,255,255,"Roboto")
        pg.display.update()

