import pygame, random, game, sys

#Colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
paleBlue = 66, 149, 244

screenWidth, screenHeight = 1280, 800


nannyaccel = []

#Getters
def getRes(): return screenWidth, screenHeight
def getPlayerRect(): return playerrect
def getNannyRect(): return nannyrects
def getBabyRect(): return babyrect

#init
def loadAssets():
    global player, playerrect
    player = pygame.image.load('assets/crook.png').convert_alpha()
    player = pygame.transform.scale(player, (100, 100))
    playerrect = player.get_rect()

    global nanny, nannyrects
    nannyrects = []
    nanny = pygame.image.load('assets/nanny.png').convert_alpha()
    nanny = pygame.transform.scale(nanny, (100, 100))
    global nanniesNumber
    nanniesNumber = random.randint(1, 3)
    for i in range(0, nanniesNumber):
        rect = nanny.get_rect()
        rect[0] = random.randint(0, screenWidth-100)
        rect[1] = random.randint(0, screenHeight-100)
        nannyrects.append(rect)
        nannyaccel.append([1, 1])

    global baby, babyrect
    baby = pygame.image.load('assets/baby.png').convert_alpha()
    baby = pygame.transform.scale(baby, (100, 100))
    babyrect = baby.get_rect()
    babyrect[0] = screenWidth-100
    babyrect[1] = screenHeight-100

def setupScreen(resolution):
    global screen
    screen = pygame.display.set_mode(resolution)

#movement
def movePlayer(keyPressed):
    global playerrect
    if keyPressed[pygame.K_s]: playerrect = playerrect.move(0, 1)
    if keyPressed[pygame.K_w]: playerrect = playerrect.move(0, -1)
    if keyPressed[pygame.K_a]: playerrect = playerrect.move(-1, 0)
    if keyPressed[pygame.K_d]: playerrect = playerrect.move(1, 0)

    if playerrect[0] < 0: playerrect[0] = 0
    if playerrect[0] > screenWidth-100: playerrect[0] = screenWidth-100
    if playerrect[1] < 0: playerrect[1] = 0
    if playerrect[1] > screenHeight-100: playerrect[1] = screenHeight-100


def moveNanny():
    global nannyrects, nannyaccel
    
    for i in range(0, nanniesNumber):
        rect = nannyrects[i]

        if rect[0] < 100 or rect[0] > screenWidth - 200:
            nannyaccel[i][0] *= -1
        if rect[1] < 100 or rect[1] > screenHeight -200:
            nannyaccel[i][1] *= -1
        rect[0] += nannyaccel[i][0]
        rect[1] += nannyaccel[i][1]
        nannyrects[i] = rect
        print(rect)

#game states
def gameover():
    font = pygame.font.SysFont(None, 48)
    deathmessage = font.render('You got nannied!', True, red)
    textrect = deathmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    losesubtitle = font.render(game.getGameoverMessage(), True, red)
    subrect = losesubtitle.get_rect()
    subrect.centerx = screen.get_rect().centerx
    subrect.centery = screen.get_rect().centery
    subrect[1] += 100
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        screen.blit(deathmessage, textrect)
        screen.blit(losesubtitle, subrect)
        pygame.display.flip()

def win():
    font = pygame.font.SysFont(None, 48)
    winmessage = font.render('You win', True, red)
    textrect = winmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    winsubtitle = font.render(game.getWinMessage(), True, red)
    subrect = winsubtitle.get_rect()
    subrect.centerx = screen.get_rect().centerx
    subrect.centery = screen.get_rect().centery
    subrect[1] += 100
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(black)
        screen.blit(winmessage, textrect)
        screen.blit(winsubtitle, subrect)
        pygame.display.flip()

def menu():
    font = pygame.font.SysFont(None, 48)
    winmessage = font.render('Crooks and Nannies', True, [27, 35, 15])
    startMessage = font.render('start', True, [27, 35, 15])
    textrect = winmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
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
        screen.blit(winmessage, textrect)
        screen.blit(startMessage, (605, 575, 200, 100))
        pygame.display.flip()

#blit
def render():
     screen.fill(white)
     screen.blit(player, playerrect)
     for i in range(0, nanniesNumber): screen.blit(nanny, nannyrects[i])
     screen.blit(baby, babyrect)
     pygame.display.flip()