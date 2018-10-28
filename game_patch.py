#!/usr/bin/python3
import pygame as pg
import random
from classes import *
from gameIntro import *
from displayText import *
from buttons import *

pg.mixer.pre_init()
pg.init()
surface = pg.display.set_mode((800, 600))





#Sounds
sound1 = pg.mixer.Sound("assets/sounds/player/aight.ogg")
sound2 = pg.mixer.Sound("assets/sounds/player/aight1.ogg")
sound3 = pg.mixer.Sound("assets/sounds/player/aight2.ogg")
sound4 = pg.mixer.Sound("assets/sounds/player/dk.ogg")
sound5 = pg.mixer.Sound("assets/sounds/player/dk1.ogg")
sound6 = pg.mixer.Sound("assets/sounds/player/dk2.ogg")
sound7 = pg.mixer.Sound("assets/sounds/player/g.ogg")
sound8 = pg.mixer.Sound("assets/sounds/player/hatersmaters.ogg")
sound9 = pg.mixer.Sound("assets/sounds/player/hateme.ogg")
sound10 = pg.mixer.Sound("assets/sounds/player/headbop.ogg")
sound11 = pg.mixer.Sound("assets/sounds/player/nasty.ogg")
sound12 = pg.mixer.Sound("assets/sounds/player/soareyou.ogg")
sound13 = pg.mixer.Sound("assets/sounds/player/stop.ogg")
sound14 = pg.mixer.Sound("assets/sounds/player/toxic.ogg")
sound15 = pg.mixer.Sound("assets/sounds/player/won.ogg")
sound16 = pg.mixer.Sound("assets/sounds/player/yeeah.ogg")
sound17 = pg.mixer.Sound("assets/sounds/player/youshe.ogg")
bruh = pg.mixer.Sound("assets/sounds/bruh.ogg")


#images
blackTexture = pg.image.load("assets/images/back_texture.png")
pointer = pg.image.load("assets/images/pointer.png")
one = pg.image.load("assets/images/1.png")
two = pg.image.load("assets/images/2.png")
three = pg.image.load("assets/images/3.png")
hit = pg.image.load("assets/images/ivebeengot.png")
stage = pg.image.load("assets/images/stage1a.png")
scene5 = pg.image.load("assets/images/scene5.png")
death = pg.image.load("assets/images/death.png")
scene3 = pg.image.load("assets/images/scene3.png")
aki = pg.image.load("assets/images/akiHead.png")
koharu = pg.image.load("assets/images/koharuHead.png")
kaito = pg.image.load("assets/images/kaitoHead.png")
lilHeesoos = pg.image.load("assets/images/lilHeesoosHead.png")
finalRound = pg.image.load("assets/images/final_round.png")
fire = pg.image.load("assets/images/onFire.png")
god = pg.image.load("assets/images/god.png")
beat = pg.image.load("assets/images/beat.png")
punch = pg.image.load("assets/images/punch.png")
scene4a = pg.image.load("assets/images/scene4a.png")
peace = pg.image.load("assets/images/peace.png")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
blue = (0,0,255)


#variables for array (level args)


#print(rapPoints.initPosition(0))


def playVoice():
	pg.mixer.stop()
	whichVoice = random.choice([sound1,sound2,sound3,sound4,sound5,sound6,sound7,sound8,sound9,sound10,sound11,sound12,sound13,sound14,sound15,sound16,sound17])
	whichVoice.play()	

# def maxScore(totalPoints,speed):
# 	rapPointNum = totalPoints#from pointPosArray dictionary get nuumber of points
# 	pointWidth = 50
# 	#speed = ?
# 	print("the total points is" + str(totalPoints))
# 	print("the speed is "+str(speed))
# 	# print("Score : " + (pointWidth/speed)*rapPointNum)
# 	return float((pointWidth/speed)*rapPointNum) #max score

# def finalScore(theScore,totalPoints):
# 	myTheMaxScore = maxScore(totalPoints,speed)
# 	print("your score is"+ str(theScore))
# 	print("your max score is"+str(totalPoints))
# 	if theScore<=0:
# 		return 0
# 	else:
# 		return float(theScore/totalPoints)
	

def youPassed(surface):
	done = False
	backImage = scene5
	sayWhat = None
	person = scene3
	count = 0
	sayWhat = random.choice(["heh ur not half bad kid...","not bad... but i wanst even triing!!","too bad ur just a kidd... you cant beat me"])
	sayWhatH = random.choice(["cmon, step it up!","yeah right...","fword you","eat a word","you are such a she"])
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					count+=1

		if count == 0:
			pass
			bruh.play()
		elif count ==1:
			sayWhat = sayWhatH
			person = lilHeesoos
		elif count == 2:
			return 1

		surface.blit(backImage,(0,0))
		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (0, 500))
		messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
		pg.display.update()

def youLost(surface):
	pg.mixer.music.pause()
	done = False
	backImage = death
	sayWhat = None
	person = lilHeesoos
	count = 0
	sayWhat = "what is the point of being here if were all goinna leave one day..."
	sayWhatH = "..."
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					count+=1

		if count == 0:
			pass
		elif count ==1:
			sayWhat = sayWhatH
			person = scene3
		elif count == 2:
			done = True

		surface.blit(backImage,(0,0))
		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (0, 500))
		messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
		pg.display.update()

def lastRound(surface):
	done = False
	backImage = finalRound
	sayWhat = None
	person = scene3
	count = 0
	sayWhat = ""
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					count+=1

		if count == 0:
			sayWhat ="wow u suck bro, its time to finish u once and 4 all!!! >:("
		elif count ==1:
			sound8.play()
			sayWhat = "this is the FINAL ROUND. ur just a hater yo. Lets go!"
			person = lilHeesoos
		elif count == 2:
			pg.mixer.music.stop()
			pg.mixer.music.load("assets/sounds/FreeHipHopBeatsThePassionHiFi-OneSound-HipHopBeatInstrumental.mp3")
			pg.mixer.music.set_volume(6)
			pg.mixer.music.play(-1)
			return 1

		surface.blit(backImage,(0,0))
		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (0, 500))
		messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
		pg.display.update()

def game(surface,maxGameRounds,minRapPointsPerRound,maxRapPointsPerRound,stage,levelNumber,minDistanceBetweenPoints,maxDistanceBetweenPoints,speed):
	done = False
	gameStart = True
	gameRound = 0



	#BarPointer
	barPointerHeight=30
	barPointerWidth = 30
	barPointerX = 0- barPointerWidth
	barPointerAndBarY = 570 - barPointerHeight


	#effects
	levelEffect = fire
	levelEffectX = -800

	def findNumberOfRapPointsInRound(minRapPointsPerRound,maxRapPointsPerRound):
		pointNum = random.randrange(minRapPointsPerRound,maxRapPointsPerRound)
		return pointNum


	def findRapPointPosition(minDistance,maxDistance):
		firstPoint = random.randrange(100,770)
		firstType = random.choice([1,2,3])

		pointPos = [firstPoint]#result
		pointType = [firstType]
		pointData = {}
		pointNumOfRound = findNumberOfRapPointsInRound(minRapPointsPerRound,maxRapPointsPerRound)
		
		# maxDomain = 770
		# minDomain = 100
		for x in range(0,pointNumOfRound):
			#round 1
			#also need to calculate distance between points
			distanceBetweenPoints = random.randrange(int(minDistance),int(maxDistance))
			guessPointPos = random.randrange(100,770)
			guessPointType = random.choice([1,2,3])
			good = False
			while good == False:
				if guessPointPos - distanceBetweenPoints<=guessPointPos<=distanceBetweenPoints + guessPointPos:

					pointPos.append(guessPointPos)
					pointType.append(guessPointType)
					# maxDomain = guessPointPos+distanceBetweenPoints
					# minDomain = guessPointPos- distanceBetweenPoints
					if guessPointPos>=800:
						guessPointPos=random.randrange(100,400)
					elif guessPointPos<=0:
						guessPointPos=random.randrange(100,400)

					good = True
				else:
					good = False
		print(pointPos)
		print(pointType)

		pointData = dict(zip(pointPos,pointType))
		# pointData.update({guessPointPos:guessPointType})
		return pointData



	global myScore
	myScore = 0 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def detectCollision(dictionary):

		for x in dictionary:
			if x-10<=barPointerX<=x+40:
				#print("oof")
				# return True
				if dictionary[x] == one:
					return 1
						
				elif dictionary[x] == two:
					return 2
						
				elif dictionary[x] == three:
					return 3
						


	allPointCount = 0
	my_final_score = 0
	newDictionary = {}
	pointPosArray = findRapPointPosition(minDistanceBetweenPoints,maxDistanceBetweenPoints)
	while not done:
		pressed = pg.key.get_pressed()
		collide = detectCollision(pointPosArray)
		#buttons and controls
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
		#rap controls and collison and score
		
		#print(str(collide))

		if pressed[pg.K_1] and collide == 1:
			# print("hit one")
			myScore += 1
			# print("my score is " +str(myScore))
			playVoice()
		elif pressed[pg.K_2] and collide == 2:
			# print("hit two")
			myScore += 1
			# print("my score is " +str(myScore))
			playVoice()
		elif pressed[pg.K_3] and collide == 3:	
			# print("hit three")
			myScore += 1
			# print("my score is " +str(myScore))
			playVoice()
		if collide == None:
			if pressed[pg.K_1]:
				# print("1")
				myScore -= 1
				# print("my score is " +str(myScore))
				sound15.play()
			elif pressed[pg.K_2]:
				# print("2")
				myScore -= 1
				# print("my score is " +str(myScore))
				sound15.play()
			elif pressed[pg.K_3]:
				# print("3")
				myScore -= 1
				# print("my score is " +str(myScore))
				sound15.play()

		#game


		if levelNumber == 4:
			levelEffect = fire
			levelEffectX +=10
			if levelEffectX >=850:
				levelEffectX = -600
		elif levelNumber == 5:
			levelEffect = god
			levelEffectX +=10
			if levelEffectX>=850:
				levelEffectX = -600


		if gameStart == True:
			barPointerX +=speed
			
			if barPointerX >= 800:
				barPointerX=0- barPointerWidth
				gameRound+=1
				# print (gameRound)
				#kill all rapPoints
				#new points
				pointPosArray = findRapPointPosition(minDistanceBetweenPoints,maxDistanceBetweenPoints)
				# print("end of the line")
				if gameRound >= maxGameRounds:
					gameStart = False
					pointPosArray = {}

		#gui
		surface.blit(pg.transform.scale(stage, (800, 600)), (0, 0))#background temp


		# print(levelEffectX)
		surface.blit(pg.transform.scale(levelEffect, (600, 200)), (levelEffectX, 100))

		surface.blit(pg.transform.scale(blackTexture, (800, 30)), (0, barPointerAndBarY))#bar back


		for x in pointPosArray:
			#print(x)
			if pointPosArray[x] == 1:
				pointPosArray[x] = one
			elif pointPosArray[x] == 2:
				pointPosArray[x] = two
			elif pointPosArray[x] == 3:
				pointPosArray[x] = three
			surface.blit(pg.transform.scale(pointPosArray[x], (30, 30)), (x, barPointerAndBarY))
				
		surface.blit(pg.transform.scale(pointer, (barPointerHeight, barPointerWidth)), (barPointerX, barPointerAndBarY))#bar pointer

		
		#add to score after round
		# print(str(len(pointPosArray)))
		newDictionary.update(pointPosArray) #acumelated points
		# print("new dictionay"+str(newDictionary))

		if gameRound >= maxGameRounds:#when done, score

				allPointCount = int(len(newDictionary))
				pointWidth = 50
				max_score = float((pointWidth/speed)*allPointCount) #max score
				if allPointCount<=0:
					my_final_score = 0
				else:
					my_final_score = float(myScore/max_score)

				print("the total points number of: "+str(allPointCount))
				print("my score is" + str(my_final_score))
				print("my score is " +str(myScore)+" out of "+str(max_score))
				if my_final_score >= 0.19:
					print("pass")
					return 1
				else:
					print("fail")
					return 0

		pg.display.flip()

def startTheGames(surface):
	count = 1 #level 1
	if count ==1:
		level = game(surface,1,2,4,stage,1,30,150,2)
		#level1 = game(surface,maxGameRounds,minRapPointsPerRound,maxRapPointsPerRound,stage,levelNumber,minDistanceBetweenPoints,maxDistanceBetweenPoints,speed)
		if level == 1:
			endGame = youPassed(surface)
			if endGame == 1:
				count+=1
		else:
			youLost(surface)

	if count ==2:
		level = game(surface,5,3,6,stage,2,30,130,3)
		if level == 1:
			endGame = youPassed(surface)
			if endGame == 1:
				count+=1
		else:
			youLost(surface)

	if count ==3:
		level = game(surface,5,5,7,stage,3,20,130,4)
		if level == 1:
			endGame = youPassed(surface)
			if endGame == 1:
				count+=1
		else:
			youLost(surface)

	if count ==4:
		level = game(surface,7,6,10,stage,4,20,130,5)
		if level == 1:
			endGame = youPassed(surface)
			if endGame == 1:
				count+=1
		else:
			youLost(surface)

	if count ==5:
		texts = lastRound(surface)
		if texts ==1:
			level = game(surface,10,5,13,stage,5,15,130,5)
			if level == 1:
				endGame = youPassed(surface)
				whichEnd = endingSpeak(surface)
				if endGame == 1:
					count+=1
				
				if whichEnd == 1:
					beatUpEnd(surface)
				elif whichEnd == 2:
					peaceEnd(surface)
			else:
				youLost(surface)

	#ending here tomorow i guess
def endChoice(surface):
	done = False
	backImage = beat
	sayWhat = None
	person = lilHeesoos
	choiceCount = 0
	sayWhat = "What Will You Do?"

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_UP:
					choiceCount = 1#beat up
				elif event.key == pg.K_DOWN:
					choiceCount = 2 #have mercy
				elif event.key == pg.K_RETURN:
					if choiceCount ==1:
						return 1
					elif choiceCount==2:
						return 2

		surface.blit(backImage,(0,0))
		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (0, 500))
		surface.blit(pg.transform.scale(blackTexture, (800, 600)), (0, 100))#choice title
		messageText(sayWhat,325,30,40,surface,255,255,255,"Roboto")
		messageText("(arrow keys and enter)",325,67,15,surface,255,255,255,"Roboto")
		button("beat him up! teach him a lesson once and 4 all!",300,350,200,100,False,surface)
		button("have mercy",320,420,150,50,False,surface)

		if choiceCount == 1:
			button("beat him up! teach him a lesson once and 4 all!",300,350,200,100,True,surface)
		if choiceCount ==2:
			button("have mercy",320,420,150,50,True,surface)


		pg.display.update()

def endingSpeak(surface):
	done = False
	backImage = beat
	sayWhat = None
	person = scene3
	count = 0
	sayWhat = ""
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					count+=1
					print(count)

		if count == 0:
			pg.mixer.music.stop()
			sayWhat ="oof ur too good bro spare me plz yo"
		elif count ==1:
			sayWhat = "hah huh???"
			person = lilHeesoos
		elif count == 2:
			# done = True
			whichRoute = endChoice(surface)
			count+=1
		elif count == 3:
			pg.mixer.music.stop()
			pg.mixer.music.load("assets/sounds/i_like_basketball.mp3")
			pg.mixer.music.set_volume(2)
			pg.mixer.music.play(-1)
			#routes
			if whichRoute == 1:#beat up
				#print ("punch")
				return 1
			elif whichRoute == 2:
				return 2

			
		surface.blit(backImage,(0,0))
		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (0, 500))
		messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
		pg.display.update()

def beatUpEnd(surface):
	done = False
	backImage = punch
	sayWhat = None
	person = lilHeesoos
	count = 0
	personX =0
	sayWhat = "fword you yo you bad bad ... beeeep im not gonna say it but fword you man"
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					count+=1

		if count == 0:
			pg.mixer.stop()
			sound16.play()
		elif count ==1:
			sayWhat = "this's what u get 4 pinching my burger"
		elif count == 2:
			person = scene3
			sayWhat = "oof oof oof"
		elif count ==3:
			backImage = scene4a
			person = koharu
			sayWhat = "nononononono omg hes killing him!"
		elif count ==4:
			person = kaito
			sayWhat = "i came.. i came here 4 a classical concert... not thiS!"
		elif count ==5:
			person = aki
			sayWhat = "..."
		elif count == 6:
			backImage = punch
			person = lilHeesoos
			sayWhat = "im gonna f word ing kill u"
		elif count ==7:
			#no back
			backImage = blackTexture
			person = aki
			sayWhat = "..."
		elif count ==8:
			person = koharu
			sayWhat = "uubhhbllughh omg i cant breath wait what??!!"
		elif count == 9:
			person = kaito
			sayWhat = "aki wake up!!!"
		elif count == 10:
			sayWhat = "she has no pusle??!!!"
		elif count == 11:
			person = koharu
			sayWhat = "call the amblunace! and the police!!"
		elif count == 12:
			person = kaito
			sayWhat = "..."
		elif count == 13:
			#no person
			personX = 800
			sayWhat = "the end"
		elif count ==14:
			sayWhat = "you should play again (press space again to end)"
		elif count ==15:
			quit()
			
		surface.blit(pg.transform.scale(backImage, (800, 600)), (0, 0))

		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (personX, 500))
		messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
		pg.display.update()

def peaceEnd(surface):
	done = False
	backImage = peace
	sayWhat = None
	person = lilHeesoos
	count = 0
	sayWhat = ""
	personX = 0
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					count+=1

		if count == 0:
			sayWhat = "you know what, I am a civilized, good, well mannered human being."
		elif count ==1:
			sayWhat = "how are you doing today?"
		elif count == 2:
			person = scene3
			sayWhat = "?"
		elif count ==3:
			sayWhat = "r u that dumb? yo brudda im lettin u off the hook 4 this one"
			person = lilHeesoos
		elif count ==4:
			sayWhat = "it just so happened that i was ina good mood today. get outta ehere now"
		elif count ==5:
			person = scene3
			sayWhat="yo lil heesoos thx bro, ur suc h a lifesaver yo"
		elif count ==6:
			sayWhat ="lets rap again sometime. bbyyyyyyyyyyyyyeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
		elif count ==7:
			person=lilHeesoos
			sayWhat = "smh"
		elif count ==8:
			person = kaito
			sayWhat = "wow even tho that wasnt even classical music that was preetty good my dudes"
			backImage = blackTexture
		elif count==9:
			person = koharu
			sayWhat ="omg omg i agree taht was so rad!!!!"
		elif count ==10:
			person = aki
			sayWhat ="..."
		elif count ==11:
			personX =800
			sayWhat="the end i hope you likeed what i made!"
		elif count ==12:
			sayWhat="press space again to end"
		elif count ==13:
			quit()



		surface.blit(pg.transform.scale(backImage, (800, 600)), (0, 0))
		surface.blit(pg.transform.scale(blackTexture, (800, 100)), (0, 500))
		surface.blit(pg.transform.scale(person, (100, 100)), (personX, 500))
		messageText(sayWhat,100,550,20,surface,255,255,255,"Roboto")
		pg.display.update()




