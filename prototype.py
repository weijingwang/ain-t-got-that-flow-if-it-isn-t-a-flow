import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
done = False
gameStart = True


#BarPointer
barPointerHeight=60
barPointerWidth = 60
barPointerX = 0- barPointerWidth
barPointerY = 0

#image
test = pg.image.load("assets/images/picture.png")
while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True

	if gameStart == True:
		barPointerX +=5

		if barPointerX >= 800:
			barPointerX=0- barPointerWidth
	screen.blit(test,(0,0))
	pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, 0, 800, 60))#bar backpg
	pg.draw.rect(screen, (0,0,0) ,pg.Rect(barPointerX,barPointerY,barPointerHeight,barPointerWidth))#bar pointer
	pg.display.flip()