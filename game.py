import pygame as pg
import random
from classes import *

pg.mixer.pre_init()
pg.init()
screen = pg.display.set_mode((800, 600))
done = False
gameStart = True

#music
pg.mixer.music.load("assets/sounds/FreeHipHopBeats-ThePassionHiFi-Foundation-HipHopBeatInstumental.mp3")
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(-1)


#BarPointer
barPointerHeight=30
barPointerWidth = 30
barPointerX = 0- barPointerWidth
barPointerAndBarY = 570 - barPointerHeight

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
blue = (0,0,255)

#images
blackTexture = pg.image.load("assets/images/back_texture.png")
pointer = pg.image.load("assets/images/pointer.png")
one = pg.image.load("assets/images/1.png")
two = pg.image.load("assets/images/2.png")
three = pg.image.load("assets/images/3.png")
test = pg.image.load("assets/images/backTemp.png")

#variables for array (level args)
gameRound = 0
maxGameRounds = 10
maxRapPointsPerRound = 4 #-1
minRapPointsPerRound = 2
stage = test
levelNumber = 1
minDistanceBetweenPoints = 30
maxDistanceBetweenPoints = 30

#print(rapPoints.initPosition(0))

def findNumberOfRapPointsInRound(minRapPointsPerRound,maxRapPointsPerRound):
	pointNum = random.randrange(minRapPointsPerRound,maxRapPointsPerRound)
	return pointNum

def findRapPointPosition(minDistanceBetweenPoints,maxDistanceBetweenPoints):
	pointPos = {}
	pointNumOfRound = findNumberOfRapPointsInRound(minRapPointsPerRound,maxRapPointsPerRound)
	for x in range(0,pointNumOfRound):
		#also need to calculate distance between points
		pointPos.update({random.randrange(30,800-60):random.choice([one,two,three])})
	return pointPos



pointPosArray = findRapPointPosition(800,800)
while not done:
	#buttons and controls
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True

	#game




	if gameStart == True:
		barPointerX +=4
		
		if barPointerX >= 800:
			barPointerX=0- barPointerWidth
			gameRound+=1
			print (gameRound)
			#kill all rapPoints
			#new points
			pointPosArray = findRapPointPosition(800,800)
			print("end of the line")
			if gameRound >= maxGameRounds:
				gameStart = False
				pointPosArray = {}

	#gui
	screen.blit(pg.transform.scale(stage, (800, 600)), (0, 0))#background temp


	screen.blit(pg.transform.scale(blackTexture, (800, 30)), (0, barPointerAndBarY))#bar back

	for x in pointPosArray:
		#print(x)
		screen.blit(pg.transform.scale(pointPosArray[x], (30, 30)), (x, barPointerAndBarY))
			
	screen.blit(pg.transform.scale(pointer, (barPointerHeight, barPointerWidth)), (barPointerX, barPointerAndBarY))#bar pointer

	
	pg.display.flip()