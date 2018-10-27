#!/usr/bin/python3
import pygame as pg
import os
from webbrowser import open_new
from displayText import * 
from buttons import *
pg.mixer.pre_init()
pg.init()
pg.font.init()

creditsBack = pg.image.load("assets/images/menu.png")
info = pg.image.load("assets/images/info.png")
info = pg.transform.scale(info, (200, 150))
creditsTxt = "This game was made by:\nspeedlimit35\n and "


#function for menu which you can call
def showCredits(surface):
	done = False
	creditsCount = 1

	url = "https://github.com/weijingwang/pyweek-26"

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:

				if event.key == pg.K_UP:
					creditsCount = 0

				if event.key == pg.K_DOWN:
					creditsCount =1

				if event.key == pg.K_RETURN:
					if creditsCount ==0:
						open_new(url) #when from asdf import fdas , no "asdf.""
						print("Opening Github Repo in Browser...")
					if creditsCount == 1:
						done = True


		surface.blit(creditsBack,(0,0))
		surface.blit(info,(300,200))


		button(creditsTxt+"Github Source",300,350,200,100,False,surface)

		button("Main Menu",320,420,150,50,False,surface)
		messageText("credits to socceristhebest for rap and Free hip hop beats from soundcloud",100,90,20,surface,255,255,255,"Roboto")
		messageText("drawings/music at en d by me/code",100,120,20,surface,255,255,255,"Roboto")
		if creditsCount == 0:
			button(creditsTxt+"Github Source",300,350,200,100,True,surface)
		elif creditsCount ==1:
			button("Main Menu",320,420,150,50,True,surface)
		pg.display.update()
