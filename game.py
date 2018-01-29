import pygame, sys, draw, random

def processUserInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
           pass
    draw.movePlayer(pygame.key.get_pressed())

def isGameWon():
    if isColliding(draw.getPlayerRect(), draw.getBabyRect()):
        return True

def isGameover():
    #nannies = draw.getNannyRect()
    for rect in draw.getNannyRect():
        if isColliding(draw.getPlayerRect(), rect):
            return True

def isColliding(object1, object2):
    if (object1[0] + object1[2] >= object2[0] and object1[0] <= object2[0] + object2[2]) and (object1[1] + object1[3] >= object2[1] and object1[1] <= object2[1] + object2[3]):
        return True

def getWinMessage():
    winMessages = "Great job, I guess", "Asshole", "So you get pleasure from stealing babies?"
    return random.choice(winMessages)
    return winMessages[random.randint(0, len(winMessages)-1)]

def getGameoverMessage():
    gameoverMessages = "Try harder next time", "Get good scrub", "Maybe it's for the best"
    return gameoverMessages[random.randint(0, len(gameoverMessages)-1)]