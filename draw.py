import pygame, random, game, sys


#Colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

screenWidth, screenHeight = 1280, 800

nannyaccelx = 1
nannyaccely = 1

#Getters
def getRes(): return screenWidth, screenHeight
def getPlayerRect(): return playerrect
def getNannyRect(): return nannyrect
def getBabyRect(): return babyrect

#init
def loadAssets():
    global player
    player = pygame.image.load('assets/crook.png').convert_alpha()
    player = pygame.transform.scale(player, (100, 100))
    global playerrect
    playerrect = player.get_rect()

    global nanny
    nanny = pygame.image.load('assets/nanny.png').convert_alpha()
    nanny = pygame.transform.scale(nanny, (100, 100))
    global nannyrect
    nannyrect = nanny.get_rect()
    nannyrect[0] = random.randint(0, screenWidth-100)
    nannyrect[1] = random.randint(0, screenHeight-100)

    global baby
    baby = pygame.image.load('assets/baby.png').convert_alpha()
    baby = pygame.transform.scale(baby, (100, 100))
    global babyrect
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
    global nannyaccelx, nannyaccely
    if nannyrect[0] < 100 or nannyrect[0] > screenWidth - 200:
        nannyaccelx *= -1
    if nannyrect[1] < 100 or nannyrect[1] > screenHeight -200:
        nannyaccely *= -1
    nannyrect[0] += nannyaccelx
    nannyrect[1] += nannyaccely

#game states
def gameover():
    font = pygame.font.SysFont(None, 48)
    deathmessage = font.render('You got nannied!', True, red)
    textrect = deathmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
        screen.fill(black)
        screen.blit(deathmessage, textrect)
        pygame.display.flip()

def win():
    font = pygame.font.SysFont(None, 48)
    winmessage = font.render('You win', True, red)
    textrect = winmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
        screen.fill(black)
        screen.blit(winmessage, textrect)
        pygame.display.flip()

#blit
def render():
     screen.fill(white)
     screen.blit(player, playerrect)
     screen.blit(nanny, nannyrect)
     screen.blit(baby, babyrect)
     pygame.display.flip()