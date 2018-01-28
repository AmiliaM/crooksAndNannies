import pygame


#Colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

def loadAssets():
    global player
    player = pygame.image.load('assets/crook.png').convert()

def setupScreen(width, height):
    global screen
    screen = pygame.display.set_mode([width, height])

def draw():
     screen.fill(black)
     screen.blit(player, (0,0))
     pygame.display.flip()