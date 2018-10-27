#!/usr/bin/python3
import pygame as pg
import os
from displayText import *
from buttons import *
pg.mixer.pre_init()
pg.init()
pg.font.init()
#surface
optionsBack = pg.image.load("assets/images/menu.png")
black = ((0,0,0))

def options(surface):
	done = False
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					done = True
		surface.blit(optionsBack,(0,0))
		messageText("Options ",325,30,40,surface,255,255,255,"Roboto")
		messageText("no options again... there was suposed to be a challenge mode here...",100,90,20,surface,255,255,255,"Roboto")
		button("Main Menu",320,400,150,50,True,surface)
		pg.display.update()
