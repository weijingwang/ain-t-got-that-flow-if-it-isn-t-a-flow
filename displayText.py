import pygame
import os
pygame.init()
def messageText(text,x,y,size,surface,red,green,blue,chooseFont):
	# os.getcwd()
	# os.chdir("roboto")
	# fontPath = os.path.dirname(os.path.abspath("Roboto-Regular.ttf"))
	# print (fontPath)qeghry'hteihjegrwrnhpvfh07ghwruhte
	if (chooseFont == "ComicSans"):
		fontFile = ("assets/fonts/ComicSansMSRegular.ttf")
	elif (chooseFont == "Roboto"):
		fontFile = ("assets/fonts/Roboto-Regular.ttf")
	elif (chooseFont == None):
		print("Sorry, there was no font specified")
	else:
		print("Sorry, we could not find the font " + chooseFont)

	myFont = pygame.font.Font(fontFile, size)

	label = myFont.render(text, 1, (red, green, blue))

	surface.blit(label, (x, y))

	pygame.display.flip()

 #how to use
 #messageText("Text to display",x,y,size,what surface,redlevel,greenlevel,bluelevel)
