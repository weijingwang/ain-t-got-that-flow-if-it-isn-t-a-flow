#!/usr/bin/python3
import pygame as pg
import os
from displayText import *
from buttons import *
pg.mixer.pre_init()
pg.init()
pg.font.init()
helpBG = pg.image.load("assets/images/menu.png")
def helps(surface):
	done = False
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					done = True
		surface.blit(helpBG,(0,0))
		messageText("Help",325,30,40,surface,255,255,255,"Roboto")
		messageText("press 123 123 123 and teach that guy a lesson!",100,90,20,surface,255,255,255,"Roboto")
		messageText("press 1,2,or 3 for as long as possible as long as your pointer is still on the point!!!",70,130,20,surface,255,255,255,"Roboto")
		button("Main Menu",320,400,150,50,True,surface)
		pg.display.update()

