import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))
done = False
gameStart = True


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

class rapPoints:
	def __init__(self, type, x):
		self.type = type
		self.x = x

	def pointSpawnPresets():
		pointType = random.randrange([red,green,yellow,blue]) #4 type
		pointX = random.randrange(30,800-barPointerWidth)
		return pointType
		return pointX

dave = rapPoints(2,2)
print("s")
#image
test = pg.image.load("assets/images/monkey.png")
while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True

	if gameStart == True:
		barPointerX +=5

		if barPointerX >= 800:
			barPointerX=0- barPointerWidth

	screen.blit(pg.transform.scale(test, (800, 600)), (0, 0))
	pg.draw.rect(screen, white, pg.Rect(0, barPointerAndBarY, 800, 30))#bar backpg
	pg.draw.rect(screen, black ,pg.Rect(barPointerX,barPointerAndBarY,barPointerHeight,barPointerWidth))#bar pointer
	#pg.draw.rect(screen,)
	pg.display.flip()