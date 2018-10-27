#!/usr/bin/python3
import pygame
pygame.init()

darkdogeGreen = ((0,150,136))
dogeGreen = ((0,200,200))
green = ((0,255,0))
darkgreen = ((0,100,0))
white = ((255,255,255))
black = ((0,0,0))
gold = ((212,175,55))
buttonFont = pygame.font.Font("assets/fonts/Roboto-Regular.ttf", 25)
def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def button(text,x,y,width,height,active,surface):
	if active == True:
		active = white
	else:
		active = gold

	textSurf, textRect = text_objects(text, buttonFont,active)
	textRect.center = ((x+(width/2)),(y+(height/2)))
	#pygame.draw.rect(surface, active, pygame.Rect(x,y,width,height))
	surface.blit(textSurf,textRect)



