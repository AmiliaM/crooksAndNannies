import pygame, draw

def init():
    #init variables
    screenWidth, screenHeight = 700, 400

    #init
    pygame.init()
    print("pygame init")
    draw.setupScreen(screenWidth, screenHeight)
    draw.loadAssets()
    print("screen init")
