#!/usr/bin/python3
import pygame as pg
import os
from displayText import *
from buttons import *
#main menu links
from credits import *
from options import *
from help import *
from gameIntro import *

pg.mixer.pre_init()
pg.init()
pg.font.init()


#screen
pg.display.set_caption("Pyweek 26 - ain't got that flow if it isn't a flow")
x = 800
y = 600
black = ((0,0,0))
screen = pg.display.set_mode((x,y))

# gameIcon = pg.image.load("assets/images/icon.png")#game icon
# pg.display.set_icon(gameIcon)
#clock = pg.time.Clock()
menu_back = pg.image.load("assets/images/menu.png")


#music
pg.mixer.music.load("assets/sounds/FreeHipHopBeatsThePassionHiFi-GottaGetUp-SoulfulHipHopBeatInstrumental.mp3")
pg.mixer.music.set_volume(1)
pg.mixer.music.play(-1)

#function for menu which you can call
def main_menu():

	print ("open main menu")
	done = False
	mainCount = 0
	while not done:
		#clock.tick(10)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_UP:

					mainCount = mainCount-1
					# print (mainCount)

				if mainCount == -1:
					mainCount = 4
					# print (mainCount)
				if event.key == pg.K_DOWN:

					mainCount = mainCount +1

					# print (mainCount)

				if mainCount == 5:
					mainCount = 0
					# print (mainCount)

			#enter

				if event.key == pg.K_RETURN:
					if mainCount == 0:#start
						#import the game
						# done = True
						pg.mixer.music.stop()#stop music from main menu
						gameIntro(screen)
					elif mainCount == 1:#Options
						#import the Options
						options(screen)
					elif mainCount == 2:#help
						#import the help
						helps(screen)
					elif mainCount == 3:
						#credits
						showCredits(screen)
					elif mainCount ==4:
						quit()

#Start
#Options
#Help
#Credits
#Quit

		screen.blit(menu_back,(0,0))
		messageText("press enter to select and arrow keys",450,470,20,screen,255,255,255,"Roboto")

		messageText("ain't got that flow if it isn't a flow",50,500,50,screen,255,255,255,"Roboto")

		button("Start",0,50,200,50,False,screen)
		button("Options",0,100,200,50,False,screen)
		button("Help",0,150,200,50,False,screen)
		button("Credits",0,200,200,50,False,screen)
		button("Quit",0,250,200,50,False,screen)

		if mainCount == 0:
			button("Start",0,50,200,50,True,screen)
		elif mainCount == 1:
			button("Options",0,100,200,50,True,screen)
		elif mainCount ==2:
			button("Help",0,150,200,50,True,screen)
		elif mainCount ==3:
			button("Credits",0,200,200,50,True,screen)
		elif mainCount == 4:
			button("Quit",0,250,200,50,True,screen)


		pg.display.update()

main_menu()
