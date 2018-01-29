import pygame, random, game, sys

#Colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
paleBlue = 66, 149, 244
green = 27, 35, 15

screenWidth, screenHeight = 1280, 800


nannyAccel = []

#Getters
def getRes(): return screenWidth, screenHeight
def getPlayerRect(): return playerRect
def getNannyRect(): return nannyRects
def getBabyRect(): return babyRect

#init
def loadAssets():
    global player, playerRect
    player = pygame.image.load('assets/crook.png').convert_alpha()
    player = pygame.transform.scale(player, (100, 100))
    playerRect = player.get_rect()

    global nanny, nannyRects
    nannyRects = []
    nanny = pygame.image.load('assets/nanny.png').convert_alpha()
    nanny = pygame.transform.scale(nanny, (100, 100))
    global nanniesNumber
    nanniesNumber = random.randint(1, 5)
    for i in range(0, nanniesNumber):
        rect = nanny.get_rect()
        rect[0] = random.randint(0, screenWidth-100)
        rect[1] = random.randint(0, screenHeight-100)
        nannyRects.append(rect)
        nannyAccel.append([1, 1])

    global baby, babyRect
    baby = pygame.image.load('assets/baby.png').convert_alpha()
    baby = pygame.transform.scale(baby, (100, 100))
    babyRect = baby.get_rect()
    babyRect[0] = screenWidth-100
    babyRect[1] = screenHeight-100

def setupScreen(resolution):
    global screen
    screen = pygame.display.set_mode(resolution)

#movement
def movePlayer(keyPressed):
    global playerRect
    if keyPressed[pygame.K_s]: playerRect = playerRect.move(0, 1)
    if keyPressed[pygame.K_w]: playerRect = playerRect.move(0, -1)
    if keyPressed[pygame.K_a]: playerRect = playerRect.move(-1, 0)
    if keyPressed[pygame.K_d]: playerRect = playerRect.move(1, 0)

    if playerRect[0] < 0: playerRect[0] = 0
    if playerRect[0] > screenWidth-100: playerRect[0] = screenWidth-100
    if playerRect[1] < 0: playerRect[1] = 0
    if playerRect[1] > screenHeight-100: playerRect[1] = screenHeight-100


def moveNanny():
    global nannyRects, nannyAccel
    
    for i in range(0, nanniesNumber):
        rect = nannyRects[i]

        if rect[0] < 100 or rect[0] > screenWidth - 200:
            nannyAccel[i][0] *= -1
        if rect[1] < 100 or rect[1] > screenHeight -200:
            nannyAccel[i][1] *= -1
        rect[0] += nannyAccel[i][0]
        rect[1] += nannyAccel[i][1]
        nannyRects[i] = rect

#game states
def gameover():
    pygame.mouse.set_visible(0)
    font = pygame.font.SysFont(None, 48)
    deathMessage = font.render('You got nannied!', True, red)
    textRect = deathMessage.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    loseSubtitle = font.render(game.getGameoverMessage(), True, red)
    subRect = loseSubtitle.get_rect()
    subRect.centerx = screen.get_rect().centerx
    subRect.centery = screen.get_rect().centery
    subRect[1] += 100
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        screen.blit(deathMessage, textRect)
        screen.blit(loseSubtitle, subRect)
        pygame.display.flip()

def win():
    pygame.mouse.set_visible(0)
    font = pygame.font.SysFont(None, 48)
    winMessage = font.render('You win', True, red)
    textRect = winMessage.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    winSubtitle = font.render(game.getWinMessage(), True, red)
    subRect = winSubtitle.get_rect()
    subRect.centerx = screen.get_rect().centerx
    subRect.centery = screen.get_rect().centery
    subRect[1] += 100
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        screen.blit(winMessage, textRect)
        screen.blit(winSubtitle, subRect)
        pygame.display.flip()

def menu():
    pygame.mouse.set_visible(1)
    font = pygame.font.SysFont(None, 48)
    winMessage = font.render('Crooks and Nannies', True, green)
    startMessage = font.render('start', True, green)
    textRect = winMessage.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    startRect = (540, 550, 200, 100)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] < 805 and pygame.mouse.get_pos()[0] > 605 and pygame.mouse.get_pos()[1] < 675 and pygame.mouse.get_pos()[1] > 575:
                    return
        screen.fill(paleBlue)
        pygame.draw.rect(screen, white, startRect, 0)
        screen.blit(winMessage, textRect)
        screen.blit(startMessage, (605, 575, 200, 100))
        pygame.display.flip()

def tutorial():
    pygame.mouse.set_visible(1)
    titleFont = pygame.font.SysFont(None, 48)
    title = titleFont.render('Tutorial', True, green)
    titleRect = title.get_rect()
    titleRect.centerx = screen.get_rect().centerx
    titleRect.centery = screen.get_rect().centery
    titleRect[1] -= 200
    font = pygame.font.SysFont(None, 28)
    explain = font.render('You are the crook                                                    Avoid the nannies                                                    Steal the baby', True, green)
    explainRect = title.get_rect()
    explainRect.centerx = screen.get_rect().centerx
    explainRect.centery = screen.get_rect().centery
    explainRect[0] -= 450
    explainRect[1] += 200
    goal = font.render('If you get enough babies, you will have good baby ice cream', True, green)
    goalRect = title.get_rect()
    goalRect.centerx = screen.get_rect().centerx
    goalRect.centery = screen.get_rect().centery
    goalRect[0] -= 200
    goalRect[1] += 300

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(paleBlue)
        screen.blit(title, titleRect)
        screen.blit(explain, explainRect)
        screen.blit(goal, goalRect)
        pygame.display.flip()

#blit
def render():
     screen.fill(white)
     screen.blit(player, playerRect)
     for i in range(0, nanniesNumber): screen.blit(nanny, nannyRects[i])
     screen.blit(baby, babyRect)
     pygame.display.flip()